from ngawrlang.basiclexer import BasicLexer
from ngawrlang.basicparser import BasicParser
from ngawrlang.basicinterpreter import BasicExecute
from sys import *

def open_file(filename):
    data = open(filename, "r").read()
    return data

if __name__ == '__main__':
    lexer = BasicLexer()
    parser = BasicParser()
    env = {}
    if len(argv) > 1:
        data = open(argv[1])
        data = data.readlines()
        for line in data:
            lex = lexer.tokenize(line)
            for token in lex:
                print(token)
    else:
        while True:
            try:
                text = input('ngawr » ')
            except EOFError:
                break
            if text:
                lex = lexer.tokenize(text)
                for token in lex:
                    print(token)
