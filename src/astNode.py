# Parent class
class Node:
    def __init__(self, type_, **kwargs):
        self.type = type_
        for k, v in kwargs.items():
            setattr(self, k, v)

    def __repr__(self):
        return f"{self.type} {self.__dict__}"

# Children
class Program(Node):
    def __init__(self, body):
        super().__init__("Program", body=body)

class Literal(Node):
    def __init__(self, value):
        super().__init__("Literal", value=value)

class Variable(Node):
    def __init__(self, id):
        super().__init__("Variable", id=id)

class Reference(Node):
    def __init__(self, id):
        super().__init__("Reference", id=id)

class VariableDeclaration(Node):
    def __init__(self, id, kind, data_type, expression):
        super().__init__("VariableDeclaration", id=id, kind=kind, data_type=data_type, expression=expression)

class VariableAssignment(Node):
    def __init__(self, id, expression):
        super().__init__("VariableAssignment", id=id, expression=expression)

class ArrayExpression(Node):
    def __init__(self, elements):
        super().__init__("ArrayExpression", elements=elements)

class ObjectExpression(Node):
    def __init__(self, properties):
        super().__init__("ObjectExpression", properties=properties)

class Property(Node):
    def __init__(self, key, value):
        super().__init__("Property", key=key, value=value)

class BinaryExpression(Node):
    def __init__(self, left, operator, right):
        super().__init__("BinaryExpression", left=left, operator=operator, right=right)

class ExpressionStatement(Node):
    def __init__(self, expression):
        super().__init__("ExpressionStatement", expression=expression)

class ConditionalExpression(Node):
    def __init__(self, condition, consequent, alternate):
        super().__init__("ConditionalExpression", condition=condition, consequent=consequent, alternate=alternate)

class IfStatement(Node):
    def __init__(self, condition, consequent, alternate):
        super().__init__("IfStatement", condition=condition, consequent=consequent, alternate=alternate)

class FunctionDefinition(Node):
    def __init__(self, id, parameters, body):
        super().__init__("FunctionDefinition", id=id, parameters=parameters, body=body)

class FunctionCall(Node):
    def __init__(self, id, arguments):
        super().__init__("FunctionCall", id=id, arguments=arguments)

class ForStatement(Node):
    def __init__(self, id, start, end, body):
        super().__init__("ForStatement", id=id, start=start, end=end, body=body)