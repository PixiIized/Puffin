class ParserError(Exception):
    """Exception raised for errors during parsing in Puffin."""
    def __init__(self, message, token=None):
        self.message = message
        self.token = token
        super().__init__(f"{message} at token: {token}")