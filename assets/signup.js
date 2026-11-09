// Newsletter signup: posts the email to Relay and always ends in a visible
// success or error message. Every request has a timeout, so the button never
// spins forever.
(function (root) {
  var ENDPOINT = "https://relay.datatalks.club/api/public/lists/dtc-newsletter/subscribe";
  var TIMEOUT_MS = 10000;
  var CONTACT = "alexey@datatalks.club";

  var MESSAGES = {
    subscribed: "You're in! Your Slack invite is on its way. It usually arrives within 3 minutes.",
    already_subscribed: "You're already subscribed to our newsletter.",
    not_resubscribed:
      "This address unsubscribed earlier, so we can't add it again from this form. Email " + CONTACT + " and we'll sort it out.",
    invalid_email: "Please enter a valid email address.",
    rate_limited: "Too many attempts. Please try again in a few minutes.",
    failed: "Something went wrong and we couldn't subscribe you. Please try again, or email " + CONTACT + ".",
    timeout: "The request took too long. Please try again, or email " + CONTACT + ".",
  };

  // Maps one Relay response to {ok, message}.
  function outcome(status, body) {
    if (status === 200 && body && MESSAGES[body.status] && body.status !== "failed") {
      return { ok: true, message: MESSAGES[body.status] };
    }
    var fields = (body && body.error && body.error.fields) || {};
    if (status === 400 && fields.email) return { ok: false, message: MESSAGES.invalid_email };
    if (status === 429) return { ok: false, message: MESSAGES.rate_limited };
    return { ok: false, message: MESSAGES.failed };
  }

  function submit(email, page, deps) {
    var controller = new deps.AbortController();
    var timer = deps.setTimeout(function () { controller.abort(); }, TIMEOUT_MS);
    return deps
      .fetch(ENDPOINT, {
        method: "POST",
        headers: { "Content-Type": "application/json", Accept: "application/json" },
        body: JSON.stringify({ email: email, company: "", page: page }),
        signal: controller.signal,
      })
      .then(function (response) {
        return response.json().then(
          function (body) { return outcome(response.status, body); },
          function () { return outcome(response.status, null); }
        );
      })
      .catch(function (error) {
        var aborted = error && error.name === "AbortError";
        return { ok: false, message: aborted ? MESSAGES.timeout : MESSAGES.failed };
      })
      .then(function (result) {
        deps.clearTimeout(timer);
        return result;
      });
  }

  function show(status, result) {
    status.textContent = result.message;
    status.className = "signup-status small pt-2 " + (result.ok ? "text-success" : "text-danger");
    status.hidden = false;
  }

  function attach(form, deps) {
    var status = form.parentNode.querySelector(".signup-status");
    var button = form.querySelector("button[type=submit]");
    form.addEventListener("submit", function (event) {
      event.preventDefault();
      var input = form.querySelector("input[type=email]");
      var honeypot = form.querySelector("input[name=company]");
      var email = (input.value || "").trim();
      if (!email) {
        show(status, { ok: false, message: MESSAGES.invalid_email });
        return;
      }
      button.disabled = true;
      status.className = "signup-status small pt-2";
      status.textContent = "Subscribing…";
      status.hidden = false;
      var send = honeypot && honeypot.value
        ? Promise.resolve({ ok: true, message: MESSAGES.subscribed })
        : submit(email, deps.page(), deps);
      send.then(function (result) {
        show(status, result);
        if (result.ok) input.value = "";
        button.disabled = false;
      });
    });
  }

  var api = { outcome: outcome, submit: submit, attach: attach, MESSAGES: MESSAGES, TIMEOUT_MS: TIMEOUT_MS, ENDPOINT: ENDPOINT };
  if (typeof module !== "undefined" && module.exports) module.exports = api;
  if (root && root.document && !root.__dtcSignup) {
    root.__dtcSignup = true;
    var deps = {
      fetch: root.fetch.bind(root),
      AbortController: root.AbortController,
      setTimeout: root.setTimeout.bind(root),
      clearTimeout: root.clearTimeout.bind(root),
      page: function () { return root.location.href; },
    };
    var start = function () {
      Array.prototype.forEach.call(root.document.querySelectorAll("form[data-relay-signup]"), function (form) {
        attach(form, deps);
      });
    };
    if (root.document.readyState === "loading") root.document.addEventListener("DOMContentLoaded", start);
    else start();
  }
})(typeof window !== "undefined" ? window : null);
