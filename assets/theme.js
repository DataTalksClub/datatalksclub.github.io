(function () {
  var storageKey = 'jtd-theme';
  var darkThemeColor = '#101815';
  var lightThemeColor = '#ffffff';

  function preferredTheme() {
    try {
      var storedTheme = localStorage.getItem(storageKey);
      if (storedTheme === 'dark' || storedTheme === 'light') {
        return storedTheme;
      }
    } catch (error) {
    }

    return 'light';
  }

  function setTheme(theme, persist) {
    var isDark = theme === 'dark';
    document.documentElement.classList.toggle('dark', isDark);
    document.documentElement.classList.toggle('light', !isDark);

    if (document.body) {
      document.body.classList.toggle('dark', isDark);
      document.body.classList.toggle('light', !isDark);
    }

    var metaThemeColor = document.querySelector('meta[name="theme-color"]');
    if (metaThemeColor) {
      metaThemeColor.setAttribute('content', isDark ? darkThemeColor : lightThemeColor);
    }

    var toggles = document.querySelectorAll('.theme-toggle');
    var label = isDark ? 'Switch to light mode' : 'Switch to dark mode';
    toggles.forEach(function (toggle) {
      toggle.setAttribute('aria-label', label);
      toggle.setAttribute('title', label);
      toggle.setAttribute('aria-pressed', isDark ? 'true' : 'false');
    });

    document.querySelectorAll('img[data-light-src][data-dark-src]').forEach(function (image) {
      image.setAttribute('src', isDark ? image.dataset.darkSrc : image.dataset.lightSrc);
    });

    if (persist) {
      try {
        localStorage.setItem(storageKey, theme);
      } catch (error) {
      }
    }
  }

  function toggleTheme() {
    var nextTheme = document.documentElement.classList.contains('dark') ? 'light' : 'dark';
    setTheme(nextTheme, true);
  }

  setTheme(preferredTheme(), false);

  document.addEventListener('DOMContentLoaded', function () {
    setTheme(preferredTheme(), false);

    document.querySelectorAll('.theme-toggle').forEach(function (toggle) {
      toggle.addEventListener('click', toggleTheme);
    });
  });
})();
