from lexer import new

PROMPT = ">>>"


def start_repl():
  while True:
    print(PROMPT, end=" ")
    line = input()
    print("total length", len(line))
    if line == "exit":
      break
    lexer = new(line)

    while True:
      tok = lexer.next_token()
      print(tok)
      if tok.type == "EOF":
        break
