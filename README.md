# markdown-toc-generator

A production-ready CLI tool to generate Markdown table of contents (TOC) by parsing headers with regex. It supports input from files or stdin, output to stdout or files, and configurable maximum header depth (default: 6). Headers are processed into nested lists with slugified anchors for standard Markdown linking.

Handles edge cases like missing files, non-standard headers, and empty content idiomatically using Python's argparse, re, and sys modules.

## Installation

```bash
git clone https://github.com/yourusername/markdown-toc-generator.git
cd markdown-toc-generator
```

No external dependencies required (uses Python standard library only). Run directly with:

```bash
python src/main.py --help
```

## Usage

Show help message:

```bash
python src/main.py --help
```

Generate TOC from stdin:

```bash
echo "# Header 1

## Header 2

### Header 3

Content here." | python src/main.py
```

Generate TOC from file to stdout:

```bash
python src/main.py input.md
```

Generate TOC to output file with depth limit:

```bash
python src/main.py input.md --output toc.md --depth 3
```

## Features

- Parses Markdown headers (`#` to `######`) using regex with multiline support
- Generates nested TOC lists (`- [text](#slugified-anchor)`) with configurable indentation
- Supports input from file or stdin (optional positional argument)
- Outputs to stdout or specified file (`--output` / `-o`)
- Configurable maximum header depth (`--depth` / `-d`, default 6)
- Slugifies header text for anchors (lowercase, hyphens, no special chars)
- Handles file errors gracefully (e.g., FileNotFoundError)

## Dependencies

- Python standard library: `argparse`, `re`, `sys`

## License

MIT