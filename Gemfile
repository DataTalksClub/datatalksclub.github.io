source "https://rubygems.org"
# Hello! This is where you manage which Jekyll version is used to run.
# When you want to use a different version, change it below, save the
# file and run `bundle install`. Run Jekyll with `bundle exec`, like so:
#
#     bundle exec jekyll serve
#
# This will help ensure the proper Jekyll version is running.
# Happy Jekylling!

# Jekyll is included via github-pages gem, so we don't need a standalone jekyll gem
# This is the default theme for new Jekyll sites. You may change this to anything you like.
#gem "minima", "~> 2.5"
gem "jekyll-theme-cayman"
gem "github-pages", group: :jekyll_plugins
gem "faraday-retry"

# This is the default theme for new Jekyll sites. You may change this to anything you like.
#gem "minima", "~> 2.5"

# GitHub Pages is already configured above. To upgrade, run `bundle update github-pages`.
# If you have any plugins, put them here!
group :jekyll_plugins do
  gem "jekyll-feed", "~> 0.12"
end

# Windows and JRuby does not include zoneinfo files, so bundle the tzinfo-data gem
# and associated library.
install_if -> { RUBY_PLATFORM =~ %r!mingw|mswin|java! } do
  gem "tzinfo", "~> 1.2"
  gem "tzinfo-data"
end

# Performance-booster for watching directories on Windows
gem "wdm", "~> 0.1.1", :install_if => Gem.win_platform?