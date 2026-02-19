import argparse
import re
import sys
def slugify(text):
    text = text.lower().strip()
    text = re.sub(r'[^a-z0-9]+', '-', text)
    return text.strip('-')
def build_toc(headers, max_depth):
    lines = []
    for level, text, anchor in headers:
        if level > max_depth:
            continue
        indent = '  ' * (level - 1)
        lines.append(f'{indent}- [{text}](#{anchor})')
    return '\n'.join(lines)
def main():
    parser = argparse.ArgumentParser(
        description='CLI tool to generate Markdown table of contents from headers.'
    )
    parser.add_argument(
        'input', nargs='?', default=None,
        help='Input markdown file (stdin if omitted)'
    )
    parser.add_argument(
        '-o', '--output',
        help='Output file (stdout if omitted)'
    )
    parser.add_argument(
        '-d', '--depth', type=int, default=6,
        help='Maximum header depth to include (default: 6)'
    )
    args = parser.parse_args()
    if args.input:
        try:
            with open(args.input, 'r', encoding='utf-8') as f:
                content = f.read()
        except FileNotFoundError:
            parser.error(f'No such file: {args.input}')
    else:
        content = sys.stdin.read()
    headers = []
    for match in re.finditer(r'^(\#{1,6})\s+(.+)$', content, re.MULTILINE):
        level_str, text = match.groups()
        level = len(level_str)
        text = text.rstrip('#').strip()
        anchor = slugify(text)
        headers.append((level, text, anchor))
    toc = build_toc(headers, args.depth)
    if args.output:
        with open(args.output, 'w', encoding='utf-8') as f:
            f.write(toc + '\n' if toc else '')
    else:
        print(toc)
if __name__ == "__main__":
    main()
