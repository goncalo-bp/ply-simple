from ply.lex import lex
from ply.yacc import yacc 
import sys
import re
import math

# ANALISADOR LÉXICO
reservadas = "tokens literals ignore return error yacc lex precedence ".split()
tokens = ['EQUALS', 'PERC', 'SYM',
          'LBRAC', 'RBRAC', 'LRBRAC', 'RRBRAC', 'LCHAV', 'RCHAV',
          'QUOTE', 'PELICA', 'COMMA', 'DOT', 'DDOT', 'BACKSLASH',
          'SSTR', 'STR', 'REGEX', 'NUMBER', 'INDEX',
          'LIST', 'CHAVSTXT'
         ] + [x.upper() for x in reservadas]

def t_SSTR(t):
    r'\w*\"(.+)\"'
    return t

def t_REGEX(t):
    r'r\'(.*)\''
    return t

def t_STR(t):
    r'[A-Za-z]+'
    if t.value in reservadas:
        t.type = t.value.upper()
    return t

def t_INDEX(t):
    r'\d+'
    t.value = int(t.value)
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

def t_LBRAC(t):      r'\('; return t
def t_RBRAC(t):      r'\)'; return t
def t_LRBRAC(t):     r'\['; return t
def t_RRBRAC(t):     r'\]'; return t
def t_LCHAV(t):      r'{' ; return t
def t_RCHAV(t):      r'}' ; return t

def t_QUOTE(t):      r'\"'; return t
def t_PELICA(t):     r'\''; return t
def t_COMMA(t):      r',' ; return t
def t_DOT(t):        r'\.'; return t
def t_DDOT(t):       r':' ; return t
def t_BACKSLASH(t):  r'\\'; return t

def t_EQUALS(t):     r'=' ; return t
def t_PERC(t):       r'%' ; return t
def t_SYM(t):
    r'[+*/^~?!-]'
    return t

t_ignore = " \t\n"

def t_error(t):
    print("Illegal character '%s'" % t.value[0])
    t.lexer.skip(1)


lexer = lex()

# GRAMÁTICA

ts = {"ltls" : []}

def p_PROG(p):
    "PROG : LEXER GRAM"
    print(p[1])
    print(p[2])

def p_LEXER(p):
    "LEXER : LIT IGN TOK TRULES"
    p[0] = f"""{p[1]}
{p[2]}
{p[3]}\n
{p[4]}
"""

def p_IGN(p):
    "IGN : PERC IGNORE EQUALS SSTR"
    p[0] = f'ignore = {p[4]}'

def p_LIT(p): 
    "LIT : PERC LITERALS EQUALS SSTR"
    p[0] = f'literals = {p[4]}'
    p[4] = p[4][:-1]
    p[4] = p[4][1:]
    for x in p[4]:
        ts['ltls'].append(x)

def p_TOK(p):
    "TOK : PERC TOKENS EQUALS LIST"
    p[0] = f'tokens = {p[4]}'


def p_TRULES_1(p): "TRULES : TRULE TRULES" ; p[0] = p[1] + p[2]
def p_TRULES_2(p): "TRULES : TERR"         ; p[0] = p[1]

def p_TRULE_1(p):
    "TRULE : REGEX RETURN LBRAC SSTR COMMA ARGS RBRAC"
    p[4] = p[4][1:]
    p[4] = p[4][:-1]
    p[0] = f"""def t_{p[4]}(t):
    {p[1]}
    return {p[6]}
"""

def p_TERR_1(p):
    "TERR : REGEX ERROR LBRAC INSTS RBRAC"
    p[0] = f"""def t_error(t):
    {p[1]}
    {p[4]}
"""

def p_INSTS_1(p):
    "INSTS : INSTS COMMA ARG"
    p[0] = f"""{p[1]}
    {p[3]}
"""
def p_INSTS_2(p):
    "INSTS : ARG"
    p[0] = f"{p[1]}"

def p_ARGS_1(p):  "ARGS : ARGS COMMA ARG"  ;  p[0] = f"{p[1]}, {p[3]}"
def p_ARGS_2(p):  "ARGS : ARG"             ;  p[0] = p[1]


def p_ARG_1(p):  "ARG : STR"                     ;   p[0] = p[1]
def p_ARG_2(p):  "ARG : NUMBER"                  ;   p[0] = p[1]
def p_ARG_3(p):  "ARG : STR LBRAC ARG RBRAC"     ;   p[0] = f"{p[1]}({p[3]})"
def p_ARG_4(p):  "ARG : STR LIST             "   ;   p[0] = f"{p[1]}{p[2]}"
def p_ARG_5(p):  "ARG : STR DOT ARG "            ;   p[0] = f"{p[1]}.{p[3]}"
def p_ARG_6(p):  "ARG : INDEX"                   ;   p[0] = p[1]
def p_ARG_7(p):  "ARG : SSTR"                    ;   p[0] = p[1]

def p_GRAM_1(p): 
    "GRAM : PRCDNC GRULES"
    p[0] = f"""{p[1]}
{p[2]}
"""

def p_PRCDNC_1(p):
    "PRCDNC : PERC PRECEDENCE EQUALS LIST"
    p[0] = f'precedence = {p[4]}\n'

def p_GRULES_1(p):  "GRULES : GRULES GRULE "  ;  p[0] = p[1] + p[2]
def p_GRULES_2(p):  "GRULES : GRULE "         ;  p[0] = p[1]

def p_GRULE_1(p):
    "GRULE : STR DDOT PARAMS CHAVSTXT"
    p[4] = p[4][2:]
    p[4] = p[4][:-2]
    if p[1] in ts:
        ts[p[1]] = ts[p[1]] + 1
    else:
        ts[p[1]] = 1
    p[0] = f"""def p_{p[1]}_{ts[p[1]]}(t):
    \"{p[1]} : {p[3]} \"
    {p[4]}
"""

def p_PARAMS_1(p):  "PARAMS : PARAMS PARAM" ; p[0] = f"{p[1]} {p[2]}"
def p_PARAMS_2(p):  "PARAMS : PARAM"        ; p[0] = f"{p[1]}"

def p_PARAM_1(p):
    "PARAM : STR"
    p[0] = p[1]
def p_PARAM_2(p):
    "PARAM : PELICA SYM PELICA"
    if p[2] in ts['ltls']:
        p[0] = f"\'{p[2]}\'"
    else:
        p[0] = "\'\'"

def p_error(p):
    print(f"Syntax error ", p)


#lexer.input(sys.stdin.read())
# Tokenize
#while True:
#    tok = lexer.token()
#    if not tok: 
#        break      # No more input
#    print(tok)

parser = yacc()
parser.parse(sys.stdin.read())
