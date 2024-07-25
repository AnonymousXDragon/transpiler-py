from tokens.token import Token
from .ast import ReturnNode, FunctionNode


class Parser:

  def __init__(self, tokens) -> None:
    self.tokens = tokens
    self.pos = 0

  def parse(self):
    package = self.parse_package()
    imports = self.parse_imports()
    return self.start_parse()

  def start_parse(self):
    return self.parse_function()

  def parse_statement(self):
    if self.current_token().type == "RETURN":
      return self.parse_return()
    raise Exception("Unexcpected token")

  def parse_expression(self):
    pass

  def parse_function(self):
    self.consume_token("FUNCTION")
    name = self.consume_token("IDENTIFIER").value
    self.consume_token("LPAREN")
    self.consume_token("RPAREN")
    self.consume_token("LBRACE")
    body = self.parse_statement()
    self.consume_token("RBRACE")
    return FunctionNode("", name, body, "VOID")

  def parse_return(self):
    self.consume_token("RETURN")
    val = self.consume_token("NUMBER").value
    return ReturnNode(val)

  def consume_token(self, expected_type):
    if self.current_token().type == expected_type:
      token = self.current_token()
      self.pos += 1
      return token
    raise Exception(
        f'expected type {expected_type} but got {self.current_token().type}')

  def parse_package(self):
    pass

  def parse_imports(self):
    pass

  def current_token(self):
    if self.pos < len(self.tokens):
      return self.tokens[self.pos]
    return Token("EOF", None)
