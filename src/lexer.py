from tokens import Token
import re

class Lexer:
    def __init__(self, code):
        self.code = code
        self.tokens = []
    
    def tokenize(self):
        chunks = re.findall(
            r"\.\.\..*?\.\.\.|^\..*?$|-?\d+\.\d+|-?\d+|>=|<=|!=|==|\?\?|::|[+\-*/%=<>?]|[{}\[\]();,:]|'.*?'|\w+",
            self.code,
            re.MULTILINE | re.DOTALL
        )


        for chunk in chunks:
            match chunk:
                case "let":
                    self.tokens.append(Token("LET", chunk))
                case "fix":
                    self.tokens.append(Token("FIX", chunk))
                case "new":
                    self.tokens.append(Token("NEW", chunk))
                case "int" | "flo" | "str" | "arr" | "mtx" | "obj" | "aut":
                    self.tokens.append(Token("TYPE", chunk))
                case "def":
                    self.tokens.append(Token("FUNCTION_DEFINITION", chunk))
                case "for":
                    self.tokens.append(Token("FOR", chunk))
                case "::":
                    self.tokens.append(Token("ASSIGNMENT_OPERATOR", chunk))
                case ":":
                    self.tokens.append(Token("COLON", chunk))
                case ">=" | "<=" | "!=" | "=" | ">" | "<" | "+" | "-" | "*" | "/" | "%":
                    self.tokens.append(Token("OPERATOR", chunk))
                case ";":
                    self.tokens.append(Token("SEMICOLON", chunk))
                case ",":
                    self.tokens.append(Token("COMMA", chunk))
                case "null":
                    self.tokens.append(Token("NULL", None))
                case "(":
                    self.tokens.append(Token("L_PAREN", chunk))
                case ")":
                    self.tokens.append(Token("R_PAREN", chunk))
                case "[":
                    self.tokens.append(Token("L_BRACKET", chunk))
                case "]":
                    self.tokens.append(Token("R_BRACKET", chunk))
                case "{":
                    self.tokens.append(Token("L_BRACE", chunk))
                case "}":
                    self.tokens.append(Token("R_BRACE", chunk))
                case "if":
                    self.tokens.append(Token("IF", chunk))
                case "elif":
                    self.tokens.append(Token("ELIF", chunk))
                case "else":
                    self.tokens.append(Token("ELSE", chunk))
                case "end":
                    self.tokens.append(Token("END", chunk))
                case "??":
                    self.tokens.append(Token("TERNARY_ELSE", chunk))
                case "?":
                    self.tokens.append(Token("TERNARY_IF", chunk))
                case _ if re.match(r"^-?\d+\.\d+$", chunk):
                    self.tokens.append(Token("FLOAT", float(chunk)))
                case _ if re.match(r"^-?\d+$", chunk):
                    self.tokens.append(Token("INT", int(chunk)))
                case _ if chunk.startswith("'") and chunk.endswith("'"):
                    self.tokens.append(Token("STRING", chunk[1:-1]))
                case _ if chunk.startswith("...") and chunk.endswith("..."):
                    pass
                case _ if chunk.startswith("."):
                    pass
                case _:
                    self.tokens.append(Token("IDENTIFIER", chunk))
            
        return self.tokens