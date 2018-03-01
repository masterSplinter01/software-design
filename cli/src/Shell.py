from src.Environment import Environment
from src.Lexer import Lexer

class Shell:
    def __init__(self):
        self.environment = Environment()

    def start(self):
        while True:
            user_string = input()
            lex = Lexer()
            tokens = lex.get_tokens(user_string)


