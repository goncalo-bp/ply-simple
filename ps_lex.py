from ply.lex import lex

# ANALISADOR LÉXICO
literals = ['(', ')', '[', ']', '{', '}', '"', '\'', ',', '.', ':', '\\', '=', '%', '+', '-', '*', '/']

reservadas = "tokens literals ignore return error yacc lex precedence ts def".split()

tokens = ['SSTR', 'STR', 'REGEX', 'NUMBER', 'INDEX', 'LITERAL',
          'LIST', 'CHAVSTXT', 'ALL'] + [x.upper() for x in reservadas]

states = (('incode', 'exclusive'),)

def t_incode_ALL(t):
    r'.+'
    return t

def t_SSTR(t):
    r'\w*\"(.+)\"'
    return t

def t_REGEX(t):
    r'r\'(.*)\''
    return t

def t_STR(t):
    r'[A-Za-z_]+'
    if t.value in reservadas:
        t.type = t.value.upper()
    return t

def t_NUMBER(t):
    r'\d+(\.\d+)?'
    t.value = float(t.value)
    return t

def t_LIST(t):
    r'\[.+\]'
    return t

def t_CHAVSTXT(t):
    r'\{.+\}'
    return t

def t_LITERAL(t):
    r'\'[,=(){}<>\[\]+\-*\/^]{1}\''
    return t

def t_begin_incode(t):
    r'%%'
    t.lexer.begin('incode')


t_ignore = " \t\n"
t_incode_ignore = "\n"

def t_ANY_error(t):
    print("Illegal character '%s'" % t.value[0])
    t.lexer.skip(1)

# Build lexer
lexer = lex()
import sys

#for line in sys.stdin:
#    lexer.input(line)
#lexer.input(sys.stdin.read())
# Tokenize
#while True:
#    tok = lexer.token()
#    if not tok: 
#        break      # No more input
#    print(tok)
