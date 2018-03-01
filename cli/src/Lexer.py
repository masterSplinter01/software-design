import src.ply.lex as lex
import src.ply.yacc as yacc

tokens = ('ASSIGNMENT', 'WORD', 'PIPE', 'QUOTED_STRING',)


t_ASSIGNMENT = r'(?<!\s)=(?!\s)'
t_WORD = r'[a-zA-Z0-9_$][a-zA-Z0-9_$]*|(?<=\s)=(?=\s)'
t_PIPE = r'\|'
t_QUOTED_STRING = r'(\"|\')(?:[^\\]|(?:\\.))*(\"|\')'
t_ignore = ' \n\t'


def t_error(t):
    print("Illegal character '%s'" % t.value[0])
    t.lexer.skip(1)


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
lexer = lex.lex()
lexer.input(data)
parser = yacc.yacc()
print(parser.parse(data))
