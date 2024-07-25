from typing import List


class Ast:
  pass


class Program(Ast):

  def __init__(self, package, imports: List[str],
               declarations: List[Ast]) -> None:
    self.package = package
    self.imports = imports
    self.declarations = declarations


class FunctionNode(Ast):

  def __init__(self, params, name, body, return_type) -> None:
    self.params = params
    self.name = name
    self.body = body
    self.return_type = return_type


class StructNode(Ast):

  def __init__(self, name, fields) -> None:
    self.name = name
    self.fields = fields


class VarNode(Ast):

  def __init__(self, name, type, value) -> None:
    self.name = name
    self.type = type
    self.value = value


class IfNode(Ast):

  def __init__(self, condition, then_block, else_block) -> None:
    self.condition = condition
    self.then_block = then_block
    self.else_block = else_block


class ForNode(Ast):

  def __init__(self, init, condition, post, body) -> None:
    self.init = init
    self.condition = condition
    self.post = post
    self.body = body


class BinaryNode(Ast):

  def __init__(self, left, op, right):
    self.left = left
    self.op = op
    self.right = right


class ClosureNode(Ast):

  def __init__(self, params, body) -> None:
    self.params = params
    self.body = body


class Literal(Ast):

  def __init__(self, value) -> None:
    self.value = value


class Identifier(Ast):

  def __init__(self, value) -> None:
    self.value = value


class ReturnNode(Ast):

  def __init__(self, value) -> None:
    self.value = value
