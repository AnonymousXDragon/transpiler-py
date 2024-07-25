from tokens import Token


class Lexer:

  def __init__(self, source) -> None:
    self.source = source
    self.currentPosition = 0
    self.nextPosition = 0
    self.char = ''

  def read(self):
    if self.nextPosition >= len(self.source):
      self.char = "EOF"
    else:
      self.char = self.source[self.nextPosition]
    self.currentPosition = self.nextPosition
    self.nextPosition += 1

  def peek(self) -> None:
    if self.nextPosition > len(self.source):
      return None
    else:
      return self.source[self.nextPosition]

  def next_token(self) -> Token:

    if self.nextPosition >= len(self.source) or self.char == "EOF":
      return Token("EOF", "EOF")

    t = Token(None, None)
    self.skipWhitespace()

    # print(self.char, self.currentPosition)
    match self.char:
      case '(':
        t = Token('LPAREN', "(")
      case ')':
        t = Token('RPAREN', ")")
      case '{':
        t = Token('LBRACE', "{")
      case '}':
        t = Token('RBRACE', "}")
      case '=':
        t = Token('EQUAL', "=")
      case '+':
        t = Token('PLUS', "+")
      case '-':
        t = Token('MINUS', "-")
      case '/':
        t = Token('DIVIDE', "/")
      case '*':
        t = Token('ASTERIX', "*")
      case "\"":
        t = Token('STRING', self.read_string())
      case '!':
        if self.peek() == '=':
          t = Token("NOT_EQUAL", "!=")
          self.read()
        else:
          t = Token("NOT", "!")
      case '>':
        if self.peek() == '=':
          t = Token("GREATER_THAN_EQUAL", ">=")
          self.read()
        else:
          t = Token("GREATER_THAN", ">")
      case '<':
        if self.peek() == '=':
          t = Token("LESS_THAN_EQUAL", "<=")
          self.read()
        else:
          t = Token("LESS_THAN", "<")
      case _:
        if self.is_letter(self.char):
          val = self.read_identifier()
          if self.check_keywords(val) is not None:
            t = Token(self.check_keywords(val), val)
          else:
            t = Token("IDENTIFIER", val)
          return t
        elif self.is_digit(self.char):
          val = self.read_number()
          t = Token("NUMBER", val)
          return t
        else:
          t = Token('ILLEGAL', self.char)
    self.read()
    return t

  def read_string(self) -> str:
    pos = self.currentPosition + 1
    while self.peek() != "\"":
      self.read()
    value = self.source[pos:self.currentPosition + 1]
    self.read()
    # 1 bug here
    return value

  def check_keywords(self, value) -> str | None:
    keywords = {
        "func": "FUNCTION",
        "var": "VAR",
        "if": "IF",
        "else": "ELSE",
        "else if": "ELSE_IF",
        "true": "TRUE",
        "false": "FALSE",
        "return": "RETURN",
        "type": "TYPE",
        "struct": "STRUCT",
        "import": "IMPORT",
        "package": "PACKAGE",
        "range": "RANGE",
        "chan": "CHAN",
        "go": "GO",
        "interface": "INTERFACE",
        "for": "FOR",
        "map": "MAP"
    }

    return keywords.get(value)

  def is_letter(self, value) -> bool:
    r = (value >= 'a' and value <= 'z') or \
    (value >= 'A' and value <= 'Z')
    return r

  def read_identifier(self) -> str:
    pos = self.currentPosition
    while self.is_letter(self.char):
      self.read()
    return self.source[pos:self.currentPosition]

  def read_number(self) -> Token:
    pos = self.currentPosition
    while self.is_digit(self.char):
      self.read()
    return self.source[pos:self.currentPosition]

  def is_digit(self, value) -> bool:
    return value >= '0' and value <= '9'

  def skipWhitespace(self) -> None:
    while self.char == ' ' or self.char == '\n' or self.char == '\t' or self.char == '\r':
      self.read()

  def tokenize(self) -> list[Token]:
    tokens = []
    while True:
      t = self.next_token()
      tokens.append(t)
      print(t.type)

      if t.type == "EOF":
        break
    return tokens


def new(src):
  lexer = Lexer(src)
  lexer.read()
  return lexer
