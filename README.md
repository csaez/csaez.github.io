# csaez.github.io

Personal resume site for Cesar Saez. A small Python script renders Markdown
content through Jinja2 templates into static HTML, hosted on GitHub Pages.

## Layout

- `config.toml` - name, headline, contact, social links, section order
- `content/*.md` - all the resume text (see below)
- `templates/` - Jinja2 templates and SVG icons
- `static/` - copied as-is (hand-written `style.css`, avatar, favicon)
- `build.py` - the generator; writes to `dist/`

## Content format

- `intro.md` - plain Markdown paragraph
- `impact.md`, `skills.md` - one bullet per item
- `experience.md`, `education.md`, `recommendations.md` - one `##` per entry
  (company / school / person), then `###` lines for details (position, dates),
  then the Markdown body

## Build and preview

```
python -m venv .venv && . .venv/bin/activate
pip install -r requirements.txt
python build.py
python -m http.server -d dist
```

Requires Python 3.11+. `dist/` is generated and git-ignored.

## Publishing

Pushing to `main` runs `.github/workflows/pages.yml`, which installs
`requirements.txt`, runs `build.py` and deploys `dist/` to GitHub Pages. In the
repository settings, Pages > Source must be set to "GitHub Actions".

## Notes

- Section order and visibility come from `sections` in `config.toml`.
- Link icons come from `templates/icons/icon-<name>.html`; add a file there to
  support a new `icon` value in `[[links]]`.
- `style.css` is plain CSS with no build step. Rules for unused elements were
  pruned, so check it when adding new markup.
- Print targets two A4 pages and ATS-friendly text extraction: one column, no
  letter-spacing on headings, fonts self-hosted in `static/fonts/` so the PDF
  embeds TrueType fonts. If you add a font weight or style that is used in
  print, add its `@font-face` too, or Chrome synthesizes a Type 3 font. Check
  with `pdffonts` and `pdftotext` after printing.
- Consecutive `experience.md` entries with the same `##` title are grouped
  under one company heading.

## Credits

Visual design based on [resume-template](https://github.com/jglovier/resume-template)
by Joel Glovier. Font: [Source Sans 3](https://github.com/adobe-fonts/source-sans)
(SIL Open Font License).
