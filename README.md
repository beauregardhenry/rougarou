# Rougarou

Jekyll site published by GitHub Pages from `main`. Post URLs retain the existing date/title format.

## Preview

```sh
bundle install
bundle exec jekyll serve --config _config.yml,_config.preview.yml
```

The preview configuration disables analytics. Production continues to use `_config.yml`.

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
