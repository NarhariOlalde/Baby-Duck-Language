import sys
from antlr4 import *
from Baby_DuckLexer import Baby_DuckLexer
from Baby_DuckParser import Baby_DuckParser

def main(argv):
    input_stream = FileStream(argv[1])
    lexer = Baby_DuckLexer(input_stream)
    stream = CommonTokenStream(lexer)
    parser = Baby_DuckParser(stream)
    tree = parser.programa()

if __name__ == '__main__':
    main(sys.argv)
