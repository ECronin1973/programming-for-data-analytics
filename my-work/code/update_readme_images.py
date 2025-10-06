"""Update README image placeholders with the latest generated PNG filenames.

This script searches `my-work/generated_charts/` for the latest files matching
patterns and replaces placeholders in `my-work/README.md`:

- {{LATEST_CSOPOP}} -> latest cso-populationbyage_galway_*.png
- {{LATEST_CSOPOP_HIGHLIGHT}} -> latest cso-populationbyage_galway_highlight_*.png
- {{LATEST_PROJECTED_BIRTHS}} -> latest projected_births_*.png

Run from the repository root like:
    python my-work/code/update_readme_images.py

It edits README.md in-place (keeps a backup as README.md.bak).
"""
from pathlib import Path
import re
import sys

ROOT = Path(__file__).resolve().parents[1]
README = ROOT / 'README.md'
OUT_DIR = ROOT / 'generated_charts'

patterns = {
    'LATEST_CSOPOP': 'cso-populationbyage_galway_*.png',
    'LATEST_CSOPOP_HIGHLIGHT': 'cso-populationbyage_galway_highlight_*.png',
    'LATEST_PROJECTED_BIRTHS': 'projected_births_*.png',
}


def find_latest(pattern):
    files = sorted(OUT_DIR.glob(pattern), key=lambda p: p.stat().st_mtime)
    return files[-1].name if files else None


def main():
    if not README.exists():
        print('README not found at', README)
        sys.exit(1)
    content = README.read_text(encoding='utf-8')
    backup = README.with_suffix('.md.bak')
    backup.write_text(content, encoding='utf-8')
    for key, pat in patterns.items():
        latest = find_latest(pat)
        if latest:
            content = content.replace('{{' + key + '}}', latest)
            print(f'Inserted latest for {key}:', latest)
        else:
            print(f'No files found for pattern {pat}; leaving placeholder for {key}.')
    README.write_text(content, encoding='utf-8')
    print('README updated (backup saved to', backup.name + ')')


if __name__ == '__main__':
    main()
