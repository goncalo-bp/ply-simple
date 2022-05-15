from operator import truediv
from ply.lex import lex
from ply.yacc import yacc 
import sys
import re
import math

# ANALISADOR LÉXICO
reservadas = "tokens literals ignore return error yacc lex precedence ts def".split()
tokens = ['EQUALS', 'PERC', 'PLUS', 'MINUS', 'TIMES', 'DIVIDE',
          'LBRAC', 'RBRAC', 'LRBRAC', 'RRBRAC', 'LCHAV', 'RCHAV',
          'QUOTE', 'PELICA', 'COMMA', 'DOT', 'DDOT', 'BACKSLASH',
          'SSTR', 'STR', 'REGEX', 'NUMBER', 'INDEX',
          'LIST', 'CHAVSTXT', 'BEGINCODE', 'ALL'] + [x.upper() for x in reservadas]
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

def t_BEGINCODE(t):
    r'%%'
    t.lexer.begin('incode')
    return t

def t_LBRAC(t):      r'\('; return t
def t_RBRAC(t):      r'\)'; return t
def t_LRBRAC(t):     r'\['; return t
def t_RRBRAC(t):     r'\]'; return t
def t_LCHAV(t):      r'\{'; return t
def t_RCHAV(t):      r'\}'; return t
def t_QUOTE(t):      r'\"'; return t
def t_PELICA(t):     r'\''; return t
def t_COMMA(t):      r',' ; return t
def t_DOT(t):        r'\.'; return t
def t_DDOT(t):       r':' ; return t
def t_BACKSLASH(t):  r'\\'; return t
def t_EQUALS(t):     r'=' ; return t
def t_PERC(t):       r'%' ; return t
def t_PLUS(t):       r'\+'; return t
def t_MINUS(t):      r'-' ; return t
def t_TIMES(t):      r'\*'; return t
def t_DIVIDE(t):     r'/' ; return t

t_ignore = " \t\n"
t_incode_ignore = "\n"

def t_ANY_error(t):
    print("Illegal character '%s'" % t.value[0])
    t.lexer.skip(1)

lexer = lex()

# GRAMÁTICA

ts = {"ltls" : []}

def p_PROG(p):
    "PROG : LEXER GRAM BEGINCODE CODE"
    print("\n# LEXER\n")
    print(p[1])
    print("\n# YACC\n")
    print(p[2])
    print("\n# PYTHON\n")
    print(p[4])

def p_CODE_1(p): "CODE : CODE ALL" ; p[0] = f"{p[1]}\n{p[2]}"
def p_CODE_2(p): "CODE : ALL"      ; p[0] = p[1]

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
    "INSTS : ARGS COMMA ARGS"
    p[0] = f"""{p[1]}
    {p[3]}
"""

def p_ARGS_1(p):  "ARGS : ARGS COMMA ARGS"          ;  p[0] = f"{p[1]}, {p[3]}"
def p_ARGS_2(p):  "ARGS : ARGS ARGS"                ;  p[0] = f"{p[1]} {p[3]}"
def p_ARGS_3(p):  "ARGS : ARGS DOT ARGS"            ;  p[0] = f"{p[1]}.{p[3]}"
def p_ARGS_4(p):  "ARGS : ARGS LBRAC ARGS RBRAC"    ;  p[0] = f"{p[1]}({p[3]})"
def p_ARGS_5(p):  "ARGS : ARGS EQUALS ARGS"         ;  p[0] = f"{p[1]} = {p[3]}"
def p_ARGS_6(p):  "ARGS : ARGS PLUS ARGS"           ;  p[0] = f"{p[1]} + {p[3]}"
def p_ARGS_7(p):  "ARGS : ARGS MINUS ARGS"          ;  p[0] = f"{p[1]} - {p[3]}"
def p_ARGS_8(p):  "ARGS : ARGS TIMES ARGS"          ;  p[0] = f"{p[1]} * {p[3]}"
def p_ARGS_9(p):  "ARGS : ARGS DIVIDE ARGS"         ;  p[0] = f"{p[1]} / {p[3]}"
def p_ARGS_10(p): "ARGS : ARG"                      ;  p[0] = p[1]

def p_ARG_1(p):  "ARG : STR"                     ;   p[0] = p[1]
def p_ARG_2(p):  "ARG : NUMBER"                  ;   p[0] = p[1]
def p_ARG_3(p):  "ARG : LIST"                    ;   p[0] = p[1]
def p_ARG_4(p):  "ARG : INDEX"                   ;   p[0] = p[1]
def p_ARG_5(p):  "ARG : SSTR"                    ;   p[0] = p[1]
def p_ARG_6(p):  "ARG : CHAVSTXT"                ;   p[0] = p[1]

def p_GRAM_1(p): 
    "GRAM : PRCDNC TSYM GRULES"
    p[0] = f"""{p[1]}
{p[2]}
{p[3]}
"""

def p_TSYM_1(p):
    "TSYM : TS EQUALS CHAVSTXT"
    p[0] = f"ts = {p[3]}\n"

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

def p_SYM_1(p): "SYM : EQUALS"  ;  p[0] = "="
def p_SYM_2(p): "SYM : PLUS"    ;  p[0] = "+"
def p_SYM_3(p): "SYM : MINUS"   ;  p[0] = "-"
def p_SYM_4(p): "SYM : TIMES"   ;  p[0] = "*"
def p_SYM_5(p): "SYM : DIVIDE"  ;  p[0] = "/"

def p_error(p):
    print(f"Syntax error ", p)

parser = yacc()
parser.parse(sys.stdin.read())
