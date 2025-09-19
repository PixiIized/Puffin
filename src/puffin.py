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

let list crops :: ['potatoes', 'carrots', 'wheat'];
let matrix cropsAndPrices :: [['potatoes', 'carrots', 'wheat'],[10, 2, 8]];

.reference time!
let int reference :: {potatoes};

if potatoes = 300:
    output('Too many potatoes!');
elif potatoes > 100:
    output('Still quite a bit.');
else:
    output('Just right!');
end;

output(1=1?'shorthand!'??'yeahbro');
"""

lexer = Lexer(code)
tokens = lexer.tokenize()
for t in tokens:
    print(t)