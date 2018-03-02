import src.ply.lex as lex

tokens = ('ASSIGNMENT', 'WORD', 'PIPE', 'QUOTED_STRING',)


t_ASSIGNMENT = r'(?<!\s)=(?!\s)'
t_WORD = r'[a-zA-Z0-9_$][a-zA-Z0-9_$]*|(?<=\s)=(?=\s)'
t_PIPE = r'\|'
t_QUOTED_STRING = r'(\"|\')(?:[^\\]|(?:\\.))*(\"|\')'
t_ignore = ' \n\t'


def t_error(t):
    print("Illegal character '%s'" % t.value[0])
    t.lexer.skip(1)

data = 'echo "sdf" | x=13| x = 13'
lx = lex.lex()
lx.input(data)


'''
data = 'echo "sdf" | x=13 | x = 13'
lx = Lexer()
tok = lx.get_tokens(data)
print(tok)

'''