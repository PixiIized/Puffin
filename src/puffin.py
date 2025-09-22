import sys 
sys.dont_write_bytecode = True
from lexer import Lexer

lexer = Lexer("'test'")
tokens = lexer.tokenize()

print(tokens)