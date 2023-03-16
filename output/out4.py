# LEXER

literals = ['[', ']', '(', ')']
tokens = ["texto"]

t_ignore = " \t\n"

def t_texto(t):
    r'\"[^"]+\"'
    return t

def t_error(t):
    r'.'
    f"illegal char {t.value[0]} line {t.lexer.lineno}"
    t.lexer.skip(1)

# YACC

ts = { }

def p_Z_1(t):
    "Z : Dir                               "
    t[0] = t[1]
def p_Dir_1(t):
    "Dir : '(' texto Ficheiros SubDirs ')'   "
    t[0] = [ "mkdir " + t[2],  "cd " + t[2], t[3] ] + t[4] 
def p_Ficheiros_1(t):
    "Ficheiros : '[' texto RestoFicheiros ']'      "
    t[0] = "touch " + t[2] + " " + t[3] 
def p_Ficheiros_2(t):
    "Ficheiros : "
    t[0] = "" 
def p_RestoFicheiros_1(t):
    "RestoFicheiros : texto RestoFicheiros              "
    t[0] = t[1] + " " + t[2] 
def p_RestoFicheiros_2(t):
    "RestoFicheiros : "
    t[0] = "" 
def p_SubDirs_1(t):
    "SubDirs : Dir SubDirs                       "
    t[0] = t[1] + t[2] 
def p_SubDirs_2(t):
    "SubDirs : "
    t[0] = ["cd .."] 

# RAW PYTHON

from ply.lex import lex
from ply.yacc import yacc

def p_error(p):
    print(f"Syntax error: ", p)
    y.success = False

# Build the lexer
lexer=lex()

# Build the parser
y=yacc()

# Read line from input and parse it
import sys
for linha in sys.stdin:
    y.success = True
    result = y.parse(linha)

    if y.success:
        for cmd in result: print(cmd) 
    else:
        print("Frase invalida... Corrija e tente novamente!")
