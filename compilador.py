from ply.lex import lex
from ply.yacc import yacc 
import sys
import re
import math

# ANALISADOR LÉXICO

reservadas = "tokens literals ignore return error yacc lex ".split()
tokens = ['PLUS', 'MINUS', 'TIMES', 'DIVIDE', 'EQUALS', 'PERC',
          'LBRAC', 'RBRAC', 'LRBRAC', 'RRBRAC', 'LCHAV', 'RCHAV',
          'QUOTE', 'PELICA', 'COMMA', 'DOT', 'BACKSLASH',
          'SSTR', 'STR', 'REGEX', 'NUMBER', 'INDEX',
          'LIST'
         ] + [x.upper() for x in reservadas]

def t_SSTR(t):
    r'\w*\"(.+)\"'
    return t

def t_REGEX(t):
    r'r\'(.*)\''
    return t

def t_STR(t):
    r'[a-z][A-Za-z]*'
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
    r'\[.*\]'
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
def t_BACKSLASH(t):  r'\\'; return t

def t_PLUS(t):       r'\+'; return t
def t_MINUS(t):      r'-' ; return t
def t_TIMES(t):      r'\*'; return t
def t_DIVIDE(t):     r'/' ; return t
def t_EQUALS(t):     r'=' ; return t
def t_PERC(t):       r'%' ; return t

t_ignore = " \t\n"

def t_error(t):
    print("Illegal character '%s'" % t.value[0])
    t.lexer.skip(1)


lexer = lex()

# GRAMÁTICA

ts = {}

def p_PROG(p):
    "PROG : LEXER"
    #"PROG : LEXER PARSER CODE"
    print(p[1])
    #print(p[2])
    #print(p[3])

def p_LEXER(p):
    "LEXER : LIT IGN TOK RULES"
    p[0] = f"""{p[1]}
{p[2]}
{p[3]}\n
{p[4]}
"""

def p_LIT(p): "LIT : PERC LITERALS EQUALS SSTR" ; p[0] = f'literals = {p[4]}\n'
def p_IGN(p): "IGN : PERC IGNORE EQUALS SSTR"   ; p[0] = f'ignore = {p[4]}\n'
def p_TOK(p): "TOK : PERC TOKENS EQUALS LIST"   ; p[0] = f'tokens = {p[4]}\n'


def p_RULES_1(p): "RULES : RULE RULES" ; p[0] = p[1] + p[2]
def p_RULES_2(p): "RULES : ERR"        ; p[0] = p[1]

def p_RULE_1(p):
    "RULE : REGEX RETURN LBRAC SSTR COMMA ARGS RBRAC"
    p[4] = p[4][1:]
    p[4] = p[4][:-1]
    p[0] = f"""def t_{p[4]}(t):
    {p[1]}
    return {p[6]}
"""

def p_ERR_1(p):
    "ERR : REGEX ERROR LBRAC INSTS RBRAC"
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
def p_ARGS_2(p):  "ARGS : ARG"             ; p[0] = p[1]


def p_ARG_1(p):  "ARG : STR"                     ;   p[0] = p[1]
def p_ARG_2(p):  "ARG : NUMBER"                  ;   p[0] = p[1]
def p_ARG_3(p):  "ARG : STR LBRAC ARG RBRAC"     ;   p[0] = f"{p[1]}({p[3]})"
def p_ARG_4(p):  "ARG : STR LRBRAC ARG RRBRAC"   ;   p[0] = f"{p[1]}[{p[3]}]"
def p_ARG_5(p):  "ARG : STR DOT ARG "            ;   p[0] = f"{p[1]}.{p[3]}"
def p_ARG_6(p):  "ARG : INDEX"                   ;   p[0] = p[1]
def p_ARG_7(p):  "ARG : SSTR"                    ;   p[0] = p[1]

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
