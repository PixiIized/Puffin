class Token:
    def __init__(self, type_, value, line=0, col=0):
        self.type = type_
        self.value = value
        self.line = line
        self.col = col
    
    def __repr__(self):
        return f'Token({self.type!r}, {self.value!r}, {self.line!r}, {self.col!r})'