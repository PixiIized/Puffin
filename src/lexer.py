from tokens import Token

class Lexer:
    def __init__(self, code):
        self.code = code
        self.line = 1
        self.col = 1
        self.index = 0
    
    def current(self):
        return self.code[self.index]

    def advance(self):
        self.index += 1
        if self.current() == '\n':
            self.col = 1
            self.line += 1
            self.advance()
        else:
            self.col += 1
    
    # End is the character on which the token ends
    # Eat is a boolean stating wether the last character is eaten or included
    # Special is a boolean stating wether seperately tokenize seperate characters, like ( or $
    def make_token(self, end, eat, special):
        self.advance()
        char = self.current()
        token = ''

        while char != end:
            if eat:
                special
            else:
                token += char
                self.advance()
        if eat:
            return token
        else:
            return token + char
    
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