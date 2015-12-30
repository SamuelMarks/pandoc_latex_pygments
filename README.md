pandoc_latex_pygments
=====================

Replace `lstlisting` with `minted` blocks in LaTeX.

## Requirements

Python 2.7. Adding Python 3 support should be trivial.

## Usage

    $ python -m pandoc_latex_pygments -h
    usage: pandoc_latex_pygments.py [-h] filename
    
    Replace `lstlisting` with `minted` blocks in LaTeX
    
    positional arguments:
      filename    File to replace `lstlisting` with `minted` in
    
    optional arguments:
      -h, --help  show this help message and exit

## Example

### Input

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

### Output

    random other stuff
    \begin{minted}[mathescape, linenos, numbersep=5pt, gobble=2, frame=lines, framesep=2mm]{python}
    print "hello world"
    \end{minted}
    more random other stuff
    \begin{minted}[mathescape, linenos, numbersep=5pt, gobble=2, frame=lines, framesep=2mm]{java}
    class HelloWorldApp {
        public static void main(String[] args) {
            System.out.println("Hello World!");
        }
    }
    \end{minted}
    final random stuff
