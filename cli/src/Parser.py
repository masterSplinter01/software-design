from src.Lexer import tokens

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
parser = yacc.yacc()

print(parser.parse(data))
