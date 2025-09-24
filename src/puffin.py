import sys 
sys.dont_write_bytecode = True
from lexer import Lexer

code = """testing
testing
1 2 3
"""

lexer = Lexer(code)
tokens = lexer.tokenize()

print(tokens)