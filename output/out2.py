
# LEXER

literals = ['(', ')']
tokens = [ 'NUM' ]

t_ignore = " \n\t"


def t_NUM(t):
    r'\d+'
    t.value = float(t.value)
    return t

def t_error(t):
    r'.'
    f"Illegal character {t.value[0]} at line {t.lexer.lineno}"
    t.lexer.skip(1)


# YACC


ts = { }

def p_ABin_1(t):
    "ABin : '(' NUM ABin ABin ')' "
    
def p_ABin_2(t):
    "ABin : '(' ')' "
    t[0] = 0 


# RAW PYTHON


from ply.lex import lex
from ply.yacc import yacc


# Build the lexer
lexer = lex()

# Build the parser
y=yacc()

def p_error(p):
    print(f"Syntax error: ", p)
    y.success = False


# Read line from input and parse it
import sys
for linha in sys.stdin:
    y.success = True
    y.parse(linha)

    if y.success:
        print("Frase valida: ", linha)
    else:
        print("Frase invalida... Corrija e tente novamente!")
