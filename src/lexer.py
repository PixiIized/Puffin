from tokens import Token
import re

class Lexer:
    def __init__(self, code):
        self.code = code
        self.tokens = []
    
    def tokenize(self):
        chunks = re.findall(
            r"\.\.\..*?\.\.\.|^\..*?$|-?\d+\.\d+|-?\d+|\w+|::|[{}\[\];,()]|'.*?'",
            self.code,
            re.MULTILINE | re.DOTALL
        )

        for chunk in chunks:
            match chunk:
                case "let":
                    self.tokens.append(Token("LET", chunk))
                case "fix":
                    self.tokens.append(Token("FIX", chunk))
                case "auto" | "int" | "string" | "list" | "matrix":
                    self.tokens.append(Token("TYPE", chunk))
                case "::":
                    self.tokens.append(Token("ASSIGNMENT_OPERATOR", chunk))
                case ";":
                    self.tokens.append(Token("SEMICOLON", chunk))
                case "null":
                    self.tokens.append(Token("NULL", None))
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