import sys 
sys.dont_write_bytecode = True
from lexer import Lexer

lexer = Lexer("'test' 'bro' indeed but what 'if I did' this")
tokens = lexer.tokenize()

print(tokens)