from unittest import TestCase, main as unittest_main

from pandoc_latex_pygments.convert import replace_lstings_with_minted, import_package


class TestPandocLatexPygments(TestCase):
    samples = (
        r'''
        random other stuff
\begin{lstlisting}
~~ python
print "hello world"
\end{lstlisting}
more random other stuff
\begin{lstlisting}
~~ java
class HelloWorldApp {
    public static void main(String[] args) {
        System.out.println("Hello World!");
    }
}
\end{lstlisting}
final random stuff
''',
        '\usepackage{fixltx2e, minted}',
        '\usepackage{minted, amsmath}\n\usepackage{microtype, amssymb}',
        '\usepackage{amsmath}\n\usepackage{microtype, amssymb}',
    )

    def test_replace_lstings_with_minted(self):
        self.assertEquals(
                '\n        random other stuff\n'
                '\\begin{minted}[mathescape, linenos, numbersep=5pt, gobble=2, frame=lines, framesep=2mm]{python}\n'
                'print "hello world"\n'
                '\\end{minted}\n'
                'more random other stuff'
                '\n\\begin{minted}[mathescape, linenos, numbersep=5pt, gobble=2, frame=lines, framesep=2mm]{java}\n'
                'class HelloWorldApp {\n'
                '    public static void main(String[] args) {\n'
                '        System.out.println("Hello World!");\n'
                '    }\n'
                '}\n'
                '\\end{minted}\n'
                'final random stuff\n'
                '',
                replace_lstings_with_minted(self.samples[0]))

    def test_import_package(self):
        self.assertEquals(self.samples[1], self.samples[1])
        self.assertEquals(self.samples[2], self.samples[2])
        expect = self.samples[3] + '\n' + r'\usepackage{minted}' + '\n'
        self.assertEquals(expect, import_package(self.samples[3]))


if __name__ == '__main__':
    unittest_main()
