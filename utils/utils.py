from lexer import new
from parser.parser import Parser
from generator import JSGenerator


def compile_to_js(code):
  # generate tokens
  lexer = new(code)
  tokens = lexer.tokenize()

  # parse to create ast
  parser = Parser(tokens)
  ast = parser.parse()

  # generate js code from ast
  js_generator = JSGenerator()
  js = js_generator.generate(ast)

  with open('generated.js', 'x') as file:
    file.write(js)
