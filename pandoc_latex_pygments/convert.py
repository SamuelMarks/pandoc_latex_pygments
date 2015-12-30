from itertools import imap
from collections import namedtuple

start = '\\begin{lstlisting}\n~~'
end = '\end{lstlisting}'
minted_prelude = r'\begin{minted}[mathescape, linenos, numbersep=5pt, gobble=2, frame=lines, framesep=2mm]'
minted_conclude = r'\end{minted}'


def find_all_code(latex):
    return tuple(imap(mintify_f(latex), (find_matching_end(latex, idx) for idx in find_all_start(latex))))


def replace_lstings_with_minted(latex):
    return replace_with(latex, find_all_code(latex))


def find_all_start(latex):
    i = latex.find(start)
    while i != -1:
        yield i
        i = latex.find(start, i + 1)


def find_matching_end(latex, idx):
    i = latex.find(end, idx)
    if i == -1:
        raise SyntaxError('No matching {end}, search begun at: {idx}'.format(end=end, idx=idx))
    return idx, i + len(end)


def mintify_f(latex):
    def mintify(idx_pair):
        """ @:returns original_block, replacement_block, boolean (telling string.replace to replace once) """
        block = latex[idx_pair[0]:idx_pair[1]]
        block_contents = block[len(start) - 2:-len(end)]

        idx = block_contents.find('~~ ')
        if idx == -1:
            lang = 'none'
            return block, minted_prelude + '{' + lang + '}\n' + block_contents + minted_conclude, True

        line = block_contents[idx:block_contents.find('\n', idx) + 1]
        lang = line[len('~~ '):-1]
        return block, block_contents.replace(line, minted_prelude + '{' + lang + '}\n') + minted_conclude, True

    return mintify


def replace_with(latex, find_replace_pairs):
    return reduce(lambda a, kv: a.replace(*kv), find_replace_pairs, latex)


def import_package(latex, package='minted'):
    if latex.find(package) == -1:
        idx = latex.find('}', latex.rfind('\usepackage{')) + 1
        return latex[:idx] + '\n' + r'\usepackage{' + package + '}\n' + latex[idx:]
    return latex
