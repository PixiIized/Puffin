from tokens import Token

class Lexer:
    def __init__(self, code):
        self.code = code
        self.line = 1
        self.col = 1
        self.index = 0
    
    def current(self):
        if self.index < len(self.code):
            return self.code[self.index]
        else:
            return None

    def advance(self):
        self.index += 1
        if self.current() == '\n':
            self.col = 1
            self.line += 1
            self.advance()
        else:
            self.col += 1
    
    def tokenize(self):
        tokens = []

        while self.current() is not None:
            token = self.tokenize_chunk()
            if token:
                tokens.append(token)
        return tokens
    
    def tokenize_chunk(self):
        char = self.current()

        if char in ("'", '"'):
            return self.make_token(char, False, False)
        if char == ' ':
            return self.make_token(char, True, True)

    # End is the character on which the token ends
    # Eat is a boolean stating wether the last and first characters are eaten or included
    # Special is a boolean stating wether seperately tokenize seperate characters, like ( or $
    def make_token(self, end, eat, special):
        if eat:
            self.advance()
        token = self.current()
        self.advance()
        char = self.current()

        while not char is None and char != end:
            token += char
            self.advance()
            char = self.current()

        if char == end:
            if not eat:
                token += char
            self.advance()

        print(token)
        return token