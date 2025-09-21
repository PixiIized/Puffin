from errors import *
from astNode import *
from tokens import Token

class Parser:
    def __init__(self, tokens):
        self.tokens = tokens
        self.index = 0
    
    def current(self):
        if self.index < len(self.tokens):
            return self.tokens[self.index]
        return None
    
    def advance(self, offset=1):
        self.index += offset
        return self.current()

    def peek(self, offset=1):
        peek_index = self.index + offset
        if peek_index < len(self.tokens):
            return self.tokens[peek_index]
        return None

    def expect(self, token_type):
        token = self.current()
        if token is None or not token.type in token_type:
            line_info = f" at line {getattr(token, 'line', '?')}"
            raise ParserError(f"Expected token '{token_type}' but got '{token.type}'{line_info}", token)
        self.advance()
        return token
    
    def parse(self):
        ast = []
        while self.current() is not None:
            node = self.parse_statement()
            if node:
                ast.append(node)
        return ast

    def parse_statement(self):
        token = self.current()

        if token.type in ("LET", "FIX"): # Variable declaration
            return self.parse_variableDeclaration()
        if token.type == "IDENTIFIER" and self.peek() and self.peek().type == "ASSIGNMENT OPERATOR":
            pass

        raise ParserError(f"Unexpected token '{token.value}' of type '{token.type}'", token)
    
    # let int age :: 20 + 5;
    def parse_variableDeclaration(self):
        kind = self.expect(("LET", "FIX")) # |let| int age :: 20 + 5;
        data_type = self.expect(("TYPE",)) # let |int| age :: 20 + 5;
        id_token = self.expect(("IDENTIFIER",)) # let int |age| :: 20 + 5;
        self.expect(("ASSIGNMENT_OPERATOR",)) # let int age |::| 20 + 5;
        expr = self.parse_expression() # let int age :: |20| + 5;
        return VariableDeclaration(kind=kind.value, data_type=data_type.value, id=id_token.value, expression=expr)
    
    def parse_expression(self):
        token = self.expect(("INT", "FLO", "STR"))
        left = Literal(token.value)

        while self.current() and self.current().type == "OPERATOR":
            op = self.current()
            self.advance()
            right_token = self.expect(("INT", "FLO", "STR"))
            right = Literal(right_token.value)
            left = BinaryExpression(left=left, operator=op.value, right=right)
        self.expect(("SEMICOLON",))
        return left