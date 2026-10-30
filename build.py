#!/usr/bin/env python3
"""Build the resume site: content/*.md + templates/ + static/ -> dist/."""

import shutil
import sys
import tomllib
from pathlib import Path
from typing import NamedTuple

import markdown
from jinja2 import Environment, FileSystemLoader, select_autoescape

ROOT = Path(__file__).parent
OUT = ROOT / "dist"

# Sections that are rendered as a flat list of entries (## heading each).
ENTRY_SECTIONS = {
    "experience": "Experience",
    "education": "Education",
    "recommendations": "Recommendations",
}
LIST_SECTIONS = {"impact": "Selected Impact", "skills": "Skills"}
# Sections hidden when printing.
NO_PRINT = {"recommendations"}


class Entry(NamedTuple):
    title: str
    details: list[str]
    body: str


def md(text: str) -> str:
    return markdown.markdown(text, extensions=["sane_lists", "smarty"])


def unwrap(html: str) -> str:
    """Drop the single wrapping paragraph so text can sit inside a heading or quote."""
    html = html.strip()
    if html.count("<p>") == 1 and html.startswith("<p>") and html.endswith("</p>"):
        return html[3:-4]
    return html


def read(name: str) -> str:
    return (ROOT / "content" / f"{name}.md").read_text(encoding="utf-8")


def parse_entries(text: str) -> list[Entry]:
    """Split a document into entries: ``##`` title, ``###`` details, rest body."""
    entries: list[Entry] = []
    title: str | None = None
    details: list[str] = []
    body: list[str] = []

    def flush() -> None:
        if title is not None:
            entries.append(Entry(title, details, md("\n".join(body).strip())))

    for line in text.splitlines():
        if line.startswith("## "):
            flush()
            title, details, body = line[3:].strip(), [], []
        elif (
            line.startswith("### ") and title is not None and not "".join(body).strip()
        ):
            details.append(line[4:].strip())
        elif title is not None:
            body.append(line)
    flush()
    return entries


def list_items(text: str) -> list[str]:
    """Render each top-level bullet as inline HTML."""
    items = []
    for line in text.splitlines():
        if line.startswith("- "):
            items.append(md(line[2:]).removeprefix("<p>").removesuffix("</p>"))
        elif line.startswith("  ") and items:
            items[-1] += " " + line.strip()
    return items


def build_sections(names: list[str]) -> list[dict]:
    sections = []
    for name in names:
        text = read(name)
        if name in LIST_SECTIONS:
            sections.append(
                {
                    "id": name,
                    "kind": "list",
                    "title": LIST_SECTIONS[name],
                    "items": list_items(text),
                }
            )
        elif name in ENTRY_SECTIONS:
            sections.append(
                {
                    "id": name,
                    "kind": name,
                    "title": ENTRY_SECTIONS[name],
                    "entries": parse_entries(text),
                    "no_print": name in NO_PRINT,
                }
            )
        else:
            sys.exit(f"unknown section: {name}")
    return sections


def main() -> None:
    with (ROOT / "config.toml").open("rb") as f:
        site = tomllib.load(f)

    env = Environment(
        loader=FileSystemLoader(ROOT / "templates"),
        autoescape=select_autoescape(["html"]),
    )
    env.filters["unwrap"] = unwrap
    html = env.get_template("index.html").render(
        site=site,
        intro=md(read("intro")),
        sections=build_sections(site["sections"]),
    )

    if OUT.exists():
        shutil.rmtree(OUT)
    shutil.copytree(ROOT / "static", OUT)
    (OUT / "index.html").write_text(html, encoding="utf-8")
    print(f"built {OUT}")


if __name__ == "__main__":
    main()
