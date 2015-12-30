#!/usr/bin/env python

from argparse import ArgumentParser

from pandoc_latex_pygments.convert import replace_lstings_with_minted, import_package


def _build_parser():
    parser = ArgumentParser(description='Replace `lstlisting` with `minted` blocks in LaTeX')
    parser.add_argument('filename', help='File to replace `lstlisting` with `minted` in')
    return parser


if __name__ == '__main__':
    filename = _build_parser().parse_args().filename
    with open(filename, 'rt') as f:
        contents = f.read()

    changed_content = replace_lstings_with_minted(import_package(contents))
    with open(filename, 'w') as f:
        f.write(changed_content)
