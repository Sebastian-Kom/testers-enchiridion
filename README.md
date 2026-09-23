# The Tester's Handbook

## [→ Open the interactive map](https://sebastian-kom.github.io/testers-enchiridion/index.html)

[Read the book online](https://sebastian-kom.github.io/testers-enchiridion/book.html) · [Download the PDF](https://sebastian-kom.github.io/testers-enchiridion/downloads/testers-enchiridion-V103.pdf)

*A handbook for people who are paid to doubt*

**Sebastian Komarnicki · V103**

A modern adaptation of Epictetus for software and systems testers: 52 short chapters about judgment, evidence, responsibility, and professional conduct. The book keeps the directness and playfulness of a handbook, with selected sentences from Elizabeth Carter's historical translation woven into the modern text.

The interactive map connects Epictetus's ideas to sections of the *Enchiridion*, the corresponding chapters of this book, and testing concepts. Its links are proposed interpretations, open to discussion and revision.

## Read and explore

- [Explore the interactive map](https://sebastian-kom.github.io/testers-enchiridion/index.html).
- [Read the book online](https://sebastian-kom.github.io/testers-enchiridion/book.html).
- [Read the Markdown manuscript](book/testers-enchiridion-V103.md).
- [Download the PDF](docs/downloads/testers-enchiridion-V103.pdf).
- [Read the source-check record](sources/testers-enchiridion-V103-source-check.md).

The complete website is already built in `docs/`. It works on GitHub Pages and can also be opened locally at `docs/index.html`. There is no account requirement, analytics service, external JavaScript library, or network dependency for the map itself. Source links and the online license page require a connection.

## Using the map

1. Select an Epictetan concept, such as **Judgment** or **Agency**.
2. Select one of the connected section numbers to read its V103 testing chapter.
3. Choose **Carter passage** to compare the checked historical excerpt, or follow its link to the full scanned source.
4. Select a testing concept to discover other related chapters.

The chapter selector and Previous/Next controls also provide access to all 52 chapters. A chapter's direct link uses a fragment such as `#chapter-18`; a source view uses `#chapter-18-source`.

The Carter view contains **selected checked passages**, not a complete transcription of the original work. Chapter 40 is explicitly marked as a deliberate departure without a retained quotation. Chapter 29 follows the historical edition's cross-reference to *Discourses* III.15.

## Sharing and reuse

This book brings Epictetus into conversation with contemporary practice and is available to read, share, question, and adapt. This repository provides the text, its sources, the concept map, and the tools used to publish them.

The original modern material in this repository, including the book, map, data, documentation, and original code, is licensed under **[CC BY-SA 4.0](https://creativecommons.org/licenses/by-sa/4.0/)**. Credit the author, indicate changes, and share adaptations under the same or a compatible license. Commercial reuse is permitted. See [LICENSE](LICENSE) for the full terms and [NOTICE.md](NOTICE.md) for attribution and scope.

Carter's historical text remains public domain. The license on this adaptation does not impose new restrictions on that text.

## Editing and rebuilding

| File or folder | Purpose |
|---|---|
| `book/testers-enchiridion-V103.md` | Canonical manuscript. Edit the text here. |
| `data/project.json` | Title, author, version, and publication metadata. |
| `data/concepts.json` | Concept labels, chapter links, and interpretation labels. |
| `sources/carter-1759-passages.json` | Checked source passages, retained anchors, and printed-page references. |
| `sources/testers-enchiridion-V103-source-check.md` | Source-check and copyedit record for V103. |
| `src/atlas.html` | Map layout and interaction template. |
| `scripts/build.py` | Builds the map, full web reader, and source page. Uses Python's standard library. |
| `scripts/build_pdf.py` | Builds the PDF from the manuscript using ReportLab. |
| `scripts/check.py` | Checks chapter completeness, source anchors, generated-text consistency, and local links. |
| `docs/` | Generated website and downloads, ready for GitHub Pages. |

Use Python 3.10 or newer. From the repository folder:

```sh
python3 -m venv .venv
. .venv/bin/activate
python3 -m pip install -r requirements.txt
python3 scripts/build.py
python3 scripts/build_pdf.py
python3 scripts/check.py
python3 -m http.server 8000 --directory docs
```

Then visit `http://localhost:8000`. The initial package includes the PDF and generated pages, so installation is only necessary when rebuilding them. After editing, commit the canonical sources and rebuilt `docs/` together.

The PDF uses standard PDF fonts. It adds a cover, contents, publication information, and source attribution around the 52 chapters. Typographic dashes are normalized for PDF output; chapter wording follows V103.

In the PDF, passages drawn from Carter's translation are italicized. A reading note before chapter 1 explains the historical language and points to the documented adaptations.

## Review and contributions

This is a review edition for testing the map on GitHub Pages before a wider announcement. Suggestions about a connection, source interpretation, wording, or interaction are welcome. See [CONTRIBUTING.md](CONTRIBUTING.md).

The publication and browser-review steps are in [PUBLISHING.md](PUBLISHING.md). The package history is in [CHANGELOG.md](CHANGELOG.md).
