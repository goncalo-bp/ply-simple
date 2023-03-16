# LEXER

literals = ['+', '*', '(', ')']
tokens = ["num"]

t_ignore = " \t\n"

def t_num(t):
    r'\d+'
    t.value = int(t.value)
    return t

def t_error(t):
    r'.'
    f"illegal char {t.value[0]} line {t.lexer.lineno}"
    t.lexer.skip(1)

# YACC

ts = { }

def p_Z_1(t):
    "Z : Sext                  "
    t[0] = t[1] 
def p_Sext_1(t):
    "Sext : '(' '+' Lista ')'     "
    t[0] = mySum(t[3]) 
def p_Sext_2(t):
    "Sext : '(' '*' Lista ')'     "
    t[0] = myProd(t[3]) 
def p_Sext_3(t):
    "Sext : num                   "
    t[0] = t[1] 
def p_Lista_1(t):
    "Lista : Sext Lista            "
    t[0] = [t[1]] + t[2] 
def p_Lista_2(t):
    "Lista : Sext Sext             "
    t[0] = [t[1]] + [t[2]] 


# RAW PYTHON

from ply.lex import lex
from ply.yacc import yacc
def mySum(l):
    r = 0
    for elem in l:
        r += elem
    return r

def myProd(l):
    r = 1
    for elem in l:
        r *= elem
    return r

def p_error(p):
    print(f"Syntax error: ", p)
    y.success = False

# Build the lexer
l=lex()

# Build the parser
y=yacc()

# Read line from input and parse it
import sys
for linha in sys.stdin:
    y.success = True
    result = y.parse(linha)
    if y.success:
        print("Frase valida: ", linha[:-1])
        print("Resultado: ", result, '\n')
    else:
        print("Frase invalida... Corrija e tente novamente!")
