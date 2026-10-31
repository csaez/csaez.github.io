#!/usr/bin/env python3
"""Build the resume site: content/*.md + templates/ + static/ -> dist/."""

import shutil
import sys
import tomllib
from pathlib import Path
from collections.abc import Callable
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


def parse_entries(text: str, render: Callable[[str], str] = md) -> list[Entry]:
    """Split a document into entries: ``##`` title, ``###`` details, rest body."""
    entries: list[Entry] = []
    title: str | None = None
    details: list[str] = []
    body: list[str] = []

    def flush() -> None:
        if title is not None:
            entries.append(Entry(title, details, render("\n".join(body).strip())))

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


def group_by_title(entries: list[Entry]) -> list[tuple[str, list[Entry]]]:
    """Merge consecutive entries sharing a title (several roles at one company)."""
    groups: list[tuple[str, list[Entry]]] = []
    for e in entries:
        if groups and groups[-1][0] == e.title:
            groups[-1][1].append(e)
        else:
            groups.append((e.title, [e]))
    return groups


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
                    "no_print": name in NO_PRINT,
                }
            )
        elif name in ENTRY_SECTIONS:
            entries = parse_entries(text)
            sections.append(
                {
                    "id": name,
                    "kind": name,
                    "title": ENTRY_SECTIONS[name],
                    "entries": entries,
                    "groups": group_by_title(entries),
                    "no_print": name in NO_PRINT,
                }
            )
        else:
            sys.exit(f"unknown section: {name}")
    return sections


def build_llms(site: dict, names: list[str]) -> str:
    """Plain Markdown version of the page for LLM crawlers (llms.txt)."""
    out = [f"# {site['name']}", "", f"> {site['headline']}", ""]
    out += [read("intro").strip(), ""]
    contact = [c for c in site["contact"] if isinstance(c, str)]
    out += [f"- Website: {site['url']}", "- Contact: " + ", ".join(contact)]
    out += [
        f"- {k['label']}: {k['url']}" for k in site["links"] if not k.get("print_only")
    ]
    out += [""]
    for name in names:
        text = read(name)
        if name in LIST_SECTIONS:
            out += [f"## {LIST_SECTIONS[name]}", "", text.strip(), ""]
        else:
            out += [f"## {ENTRY_SECTIONS[name]}", ""]
            for e in parse_entries(text, render=str):
                out += [f"### {e.title}"]
                if e.details:
                    out += ["", "**" + " | ".join(e.details) + "**"]
                out += ["", e.body, ""]
    return "\n".join(out).rstrip() + "\n"


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
    (OUT / "llms.txt").write_text(build_llms(site, site["sections"]), encoding="utf-8")
    print(f"built {OUT}")


if __name__ == "__main__":
    main()
