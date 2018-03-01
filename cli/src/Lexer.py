import src.ply.lex as lex

tokens = ('ASSIGNMENT', 'WORD', 'PIPE', 'QUOTED_STRING',)

t_PIPE = r'\|'
t_QUOTED_STRING = r'(\"|\')(?:[^\\]|(?:\\.))*(\"|\')'
t_ASSIGNMENT = r'(?<!\s)=(?!\s)'
t_WORD = r'[a-zA-Z0-9_$][a-zA-Z0-9_$]*|(?<=\s)=(?=\s)'
t_ignore = ' \n\t'


def t_error(t):
    print("Illegal character '%s'" % t.value[0])
    t.lexer.skip(1)


class Lexer:
    def __init__(self):
        self.lexer = lex.lex()

    def get_tokens(self, input_str):
        self.lexer.input(input_str)
        result_tokens = []
        while True:
            tok = self.lexer.token()
            if not tok:
                break
            result_tokens.append(tok)
        return result_tokens

import src.ply.yacc as yacc


def p_assignment(p):
    '''assignment : WORD ASSIGNMENT WORD'''

def p_command(p):
    '''command : WORD
                | command WORD
                | command QUOTED_STRING '''



def p_command_line(p):
    '''command_line : command
                    | command PIPE command_line '''


data = 'echo "sdf" | x=13| x = 13'
lx = Lexer()
tokend = lx.get_tokens(data)
parser = yacc.yacc()
print(parser.parse(data))


'''
data = 'echo "sdf" | x=13 | x = 13'
lx = Lexer()
tok = lx.get_tokens(data)
print(tok)

'''