from lexer import Lexer

code = """
let int potatoes :: 15;
fix int price :: 5;
let string offer :: 'Buy my potatoes!';
.one line
...
This is a multi-line comment
...
output(offer);
"""

lexer = Lexer(code)
tokens = lexer.tokenize()
for t in tokens:
    print(t)