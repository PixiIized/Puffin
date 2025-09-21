import sys 
sys.dont_write_bytecode = True
from errors import *
from lexer import Lexer
from parser import Parser

code = """
let int age :: 20 + 5;
"""

lexer = Lexer(code)
tokens = lexer.tokenize()
parser = Parser(tokens)

try:
    ast = parser.parse()
    print("AST:")
    for node in ast:
        print(node)
except ParserError as e:
    print("Parser error:", e)