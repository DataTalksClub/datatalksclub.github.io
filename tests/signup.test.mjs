import test from "node:test";
import assert from "node:assert/strict";
import { createRequire } from "node:module";

const signup = createRequire(import.meta.url)("../assets/signup.js");

const deps = (fetch) => ({
  fetch,
  AbortController,
  setTimeout,
  clearTimeout,
});
const reply = (status, body) => () => Promise.resolve({ status, json: () => Promise.resolve(body) });

test("subscribed and already_subscribed are success messages", async () => {
  const ok = await signup.submit("a@b.co", "p", deps(reply(200, { status: "subscribed" })));
  assert.deepEqual(ok, { ok: true, message: signup.MESSAGES.subscribed });
  const dup = await signup.submit("a@b.co", "p", deps(reply(200, { status: "already_subscribed" })));
  assert.equal(dup.ok, true);
  assert.equal(dup.message, signup.MESSAGES.already_subscribed);
});

test("sends email, empty honeypot and page as JSON to the Relay list", async () => {
  let seen;
  await signup.submit("a@b.co", "https://www.datatalks.club/", deps((url, init) => {
    seen = { url, init };
    return reply(200, { status: "subscribed" })();
  }));
  assert.equal(seen.url, "https://relay.datatalks.club/api/public/lists/dtc-newsletter/subscribe");
  assert.equal(seen.init.method, "POST");
  assert.deepEqual(JSON.parse(seen.init.body), { email: "a@b.co", company: "", page: "https://www.datatalks.club/" });
});

test("validation, rate limit and server errors show visible error messages", async () => {
  const bad = await signup.submit("x", "p", deps(reply(400, { error: { fields: { email: "invalid" } } })));
  assert.deepEqual(bad, { ok: false, message: signup.MESSAGES.invalid_email });
  const limited = await signup.submit("a@b.co", "p", deps(reply(429, { error: {} })));
  assert.equal(limited.message, signup.MESSAGES.rate_limited);
  const broken = await signup.submit("a@b.co", "p", deps(reply(500, { error: { code: "internal_error" } })));
  assert.deepEqual(broken, { ok: false, message: signup.MESSAGES.failed });
  const html = await signup.submit("a@b.co", "p", deps(() => Promise.resolve({ status: 502, json: () => Promise.reject(new Error("not json")) })));
  assert.equal(html.ok, false);
});

test("network failure shows an error", async () => {
  const result = await signup.submit("a@b.co", "p", deps(() => Promise.reject(new TypeError("Failed to fetch"))));
  assert.deepEqual(result, { ok: false, message: signup.MESSAGES.failed });
});

test("a hung request is aborted after the timeout and shows an error", async () => {
  const hung = (url, init) =>
    new Promise((resolve, reject) => {
      init.signal.addEventListener("abort", () => reject(Object.assign(new Error("aborted"), { name: "AbortError" })));
    });
  const fastTimers = { ...deps(hung), setTimeout: (fn) => setTimeout(fn, 20) };
  const started = Date.now();
  const result = await signup.submit("a@b.co", "p", fastTimers);
  assert.deepEqual(result, { ok: false, message: signup.MESSAGES.timeout });
  assert.ok(Date.now() - started < 2000);
  assert.equal(signup.TIMEOUT_MS, 10000);
});
