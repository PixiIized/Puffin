from tokens import Token
import re

class Lexer:
    def __init__(self, code):
        self.code = code
        self.tokens = []

    def tokenize(self):
        pattern = re.compile(
            r"\.\.\..*?\.\.\.|^\..*?$|-?\d+\.\d+|-?\d+|>=|<=|!=|==|\?\?|::|[+\-*/%=<>?]|[{}\[\]();,:]|'.*?'|\w+",
            re.MULTILINE | re.DOTALL
        )

        for match in pattern.finditer(self.code):
            chunk = match.group()
            start_index = match.start()

            line = self.code.count("\n", 0, start_index) + 1
            last_newline = self.code.rfind("\n", 0, start_index)
            col = start_index - (last_newline + 1) + 1  # 1-indexed column

            match chunk:
                case "let":
                    self.tokens.append(Token("LET", chunk, line=line, col=col))
                case "fix":
                    self.tokens.append(Token("FIX", chunk, line=line, col=col))
                case "new":
                    self.tokens.append(Token("NEW", chunk, line=line, col=col))
                case "int" | "flo" | "str" | "arr" | "mtx" | "obj" | "aut":
                    self.tokens.append(Token("TYPE", chunk, line=line, col=col))
                case "def":
                    self.tokens.append(Token("FUNCTION_DEFINITION", chunk, line=line, col=col))
                case "for":
                    self.tokens.append(Token("FOR", chunk, line=line, col=col))
                case "::":
                    self.tokens.append(Token("ASSIGNMENT_OPERATOR", chunk, line=line, col=col))
                case "$":
                    self.tokens.append(Token("REFERENCE_TAG", chunk, line=line, col=col))
                case ":":
                    self.tokens.append(Token("COLON", chunk, line=line, col=col))
                case ">=" | "<=" | "!=" | "=" | ">" | "<" | "+" | "-" | "*" | "/" | "%":
                    self.tokens.append(Token("OPERATOR", chunk, line=line, col=col))
                case ";":
                    self.tokens.append(Token("SEMICOLON", chunk, line=line, col=col))
                case ",":
                    self.tokens.append(Token("COMMA", chunk, line=line, col=col))
                case "null":
                    self.tokens.append(Token("NULL", None, line=line, col=col))
                case "(":
                    self.tokens.append(Token("L_PAREN", chunk, line=line, col=col))
                case ")":
                    self.tokens.append(Token("R_PAREN", chunk, line=line, col=col))
                case "[":
                    self.tokens.append(Token("L_BRACKET", chunk, line=line, col=col))
                case "]":
                    self.tokens.append(Token("R_BRACKET", chunk, line=line, col=col))
                case "{":
                    self.tokens.append(Token("L_BRACE", chunk, line=line, col=col))
                case "}":
                    self.tokens.append(Token("R_BRACE", chunk, line=line, col=col))
                case "if":
                    self.tokens.append(Token("IF", chunk, line=line, col=col))
                case "elif":
                    self.tokens.append(Token("ELIF", chunk, line=line, col=col))
                case "else":
                    self.tokens.append(Token("ELSE", chunk, line=line, col=col))
                case "end":
                    self.tokens.append(Token("END", chunk, line=line, col=col))
                case "??":
                    self.tokens.append(Token("TERNARY_ELSE", chunk, line=line, col=col))
                case "?":
                    self.tokens.append(Token("TERNARY_IF", chunk, line=line, col=col))
                case _ if re.match(r"^-?\d+\.\d+$", chunk):
                    self.tokens.append(Token("FLOAT", float(chunk), line=line, col=col))
                case _ if re.match(r"^-?\d+$", chunk):
                    self.tokens.append(Token("INT", int(chunk), line=line, col=col))
                case _ if chunk.startswith("'") and chunk.endswith("'"):
                    self.tokens.append(Token("STRING", chunk[1:-1], line=line, col=col))
                case _ if chunk.startswith("...") and chunk.endswith("..."):
                    pass
                case _ if chunk.startswith("."):
                    pass
                case _:
                    self.tokens.append(Token("IDENTIFIER", chunk, line=line, col=col))

        return self.tokens