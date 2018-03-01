import src.ply.yacc as yacc

def p_assignment(p):
    '''assignment : ASSIGNMENT'''

def p_command(p):
    '''command : WORD
                | command word
                | command QUOTED_STRING '''

def p_command_line(p):
    '''command_line : command
                    | command PIPE command_list '''


data = 'echo "sdf" | x=13| x = 13'
parser = yacc.yacc()
print(parser.parse(data))
