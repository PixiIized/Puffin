from tokens import Token

class Lexer:
    def __init__(self, code):
        self.code = code
        self.line = 1
        self.col = 1
        self.index = 0
        self.start = 0
        self.end = 0
    
    def current(self):
        if self.index < len(self.code):
            return self.code[self.index]
        else:
            return None
    
    def peek(self, amount=1):
        if self.index + amount < len(self.code):
            return self.code[self.index + amount]
        else:
            return None

    def advance(self):
        self.index += 1
        if self.current() == ?? self.peek() == 'n':
            self.col = 1
            self.line += 1
            self.advance()
            return self.current()
        else:
            self.col += 1
            return self.current()
    
    def tokenize(self):
        tokens = []

        while self.current() is not None:
            token = self.create_token()
            if token:
                tokens.append(token)
        return tokens
    
    def create_token(self):
        char = self.current()

        if char in ("'", '"'):
            pass
        else:
            return self.identify(self.tokenize_chunk())
    
    def identify(self, token):
        if token == 'placeholder':
            pass
        else:
            return Token("IDENTIFIER", token, self.line, self.col-(len(token)+1), self.start, self.end)
    
    def tokenize_chunk(self):
        token = ''
        char = self.current()
        self.start = self.index

        while char is not None and char != ' ':
            token += char
            char = self.advance()
        self.end = self.index - 1
        self.advance()
        return token