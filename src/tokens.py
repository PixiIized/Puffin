# Token class
class Token:
    def __init__(self, type_, value, line, col, start, end):
        self.type = type_
        self.value = value
        self.line = line
        self.col = col
        self.start = start
        self.end = end
    
    def __repr__(self):
        return f'Token({self.type!r}, {self.value!r}, {self.line!r}, {self.col!r}, {self.start!r}, {self.end!r})'