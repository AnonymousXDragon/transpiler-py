from parser.ast import FunctionNode, ReturnNode


class JSGenerator:

  def __init__(self) -> None:
    pass

  def generate(self, node):
    if isinstance(node, FunctionNode):
      return f"function {node.name}() {{\n {self.generate(node.body)} \n}}"
    elif isinstance(node, ReturnNode):
      return f"return {node.value}"
    else:
      raise Exception(f"Unexcpected node type {type(node)}")
