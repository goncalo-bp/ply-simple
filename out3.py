
# LEXER

literals = ['[', ']', ',']
tokens = ["NUM"]

t_ignore = " \t\n"


def t_NUM(t):
    r'\d+'
    t.value = int(t.value)
    return t

def t_error(t):
    r'.'
    f"Illegal char {t.value[0]} line {t.lexer.lineno}"
    t.lexer.skip(1)


# YACC


ts = { }

def p_lista_1(t):
    "lista : '[' ']'             "
    
def p_lista_2(t):
    "lista : '[' NUM resto ']'   "
    
def p_resto_1(t):
    "resto : ',' NUM resto       "
    
def p_resto_2(t):
    "resto : "
    


# RAW PYTHON


from ply.lex import lex
from ply.yacc import yacc

def p_error(p):
    print(f"Syntax error: ", p)
    y.success = False

# Build the lexer
lexer = lex()

# Build the parser
y=yacc()


# Read line from input and parse it
import sys
for linha in sys.stdin:
    y.success = True
    y.parse(linha)

    if y.success:
        print("Frase valida: ", linha)
    else:
        print("Frase invalida... Corrija e tente novamente!")
