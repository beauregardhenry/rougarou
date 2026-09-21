"""Check local page, asset, and fragment links in a Jekyll build."""
from html.parser import HTMLParser
from pathlib import Path
from urllib.parse import unquote, urljoin, urlsplit
import sys

root = Path(sys.argv[1] if len(sys.argv) > 1 else '_site').resolve()
if not (root / 'index.html').is_file():
    raise SystemExit(f'No built homepage found in {root}')

class Page(HTMLParser):
    def __init__(self, path):
        super().__init__(convert_charrefs=True)
        self.links, self.ids = [], set()
        self.feed(path.read_text())

    def handle_starttag(self, tag, attrs):
        attrs = dict(attrs)
        if attrs.get('id'):
            self.ids.add(attrs['id'])
        if tag == 'a' and attrs.get('name'):
            self.ids.add(attrs['name'])
        for attribute in ('href', 'src'):
            if attrs.get(attribute):
                self.links.append(attrs[attribute])

pages = {path: Page(path) for path in root.rglob('*.html')}
errors = set()
checks = 0
for path, page in pages.items():
    relative = '/' + path.relative_to(root).as_posix()
    base = relative[:-10] if relative.endswith('index.html') else relative
    for link in page.links:
        url = urlsplit(link)
        if url.scheme or url.netloc:
            continue
        target = urlsplit(urljoin(base, link))
        filename = root / unquote(target.path).lstrip('/')
        candidates = [filename, filename / 'index.html', Path(str(filename) + '.html')]
        found = next((candidate for candidate in candidates if candidate.is_file()), None)
        checks += 1
        if not found:
            errors.add(f'{relative}: missing {link}')
        elif target.fragment and found.suffix == '.html':
            if unquote(target.fragment) not in pages[found].ids:
                errors.add(f'{relative}: missing fragment {link}')

if errors:
    raise SystemExit('\n'.join(sorted(errors)))
print(f'Passed: {checks} local links across {len(pages)} HTML pages.')
