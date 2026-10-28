# Rougarou

Jekyll site published by GitHub Pages from `main`. Post URLs retain the existing date/title format.

## Preview

```sh
bundle install
bundle exec jekyll serve --config _config.yml,_config.preview.yml
```

The preview configuration disables analytics. Production continues to use `_config.yml`.

## Honeycomb (browser observability)

Page-load traces, Core Web Vitals, and JS errors, via Honeycomb's OpenTelemetry Web SDK. Disabled until a real API key is set, since the default in `_config.yml` is `honeycomb.api_key: false`.

To enable it:

1. [Create a Honeycomb API key](https://docs.honeycomb.io/get-started/configure/environments/manage-api-keys/#find-api-keys) scoped to **Send Events** only — it ends up in client-side JS, visible to anyone who views the page source, same as the PostHog token above.
2. Set `honeycomb.api_key` in `_config.yml` to that key.

The SDK itself ships as a prebuilt bundle (`assets/js/honeycomb.bundle.js`), since GitHub Pages' own Jekyll build can't run npm. Rebuild it after changing `scripts/honeycomb/index.js` or upgrading its dependencies:

```sh
npm install
npm run build:honeycomb
```

Commit the rebuilt `assets/js/honeycomb.bundle.js`. CI rebuilds it on every push and fails if it's out of sync with its source.

## Selected work and biography

Edit `_data/selected_work.yml` to change the homepage selections. Each `slug` is the post filename without its date or extension. `about.html` contains the biography and reuses the same selections. Every post remains in `/archive/`.

## Categories

GitHub Pages' built-in publishing does not support `jekyll-category-pages`. Category pages are therefore checked in, with a shared Liquid layout. After adding or changing categories, run:

```sh
bundle exec ruby scripts/sync_categories.rb
bundle exec ruby scripts/sync_categories.rb --check
```

Commit the generated files under `category/` and `categories/`. `/category/<slug>/` is canonical; the plural route redirects there. Categories with the same slug share a page instead of overwriting each other.

## Sources and checks

AI analysis posts have a `sources` list in their front matter and links at the relevant passage. `docs/editorial-review.md` records remaining substantive editorial concerns; it is excluded from the website.

```sh
bundle exec jekyll build --safe --config _config.yml,_config.preview.yml
python3 scripts/check_links.py _site
```

The link check validates local pages, assets, and fragment targets. It does not check external websites or the truth of article claims.
