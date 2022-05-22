from lib2to3.pgen2 import literals
from mimetypes import init
from operator import truediv
from ply.lex import lex
from ply.yacc import yacc 
import sys
import re
import math

literals = []
tokens = ['LexBegin', 'YaccBegin', 'CodeBegin',
          'LPAR', 'RPAR', 'LSPAR', 'RSPAR', 'LCHAV', 'RCHAV', 
          'LESS', 'MORE', 'EQ', 'PLUS', 'MINUS', 'TIMES',
          'SLASH', 'BSLASH', 'PERC',
          'QUOTE', 'PELICA', 'UNDERSCORE', 'DOT', 'COMMA',
          'Str', 'Int', 'Float',
          'LexLiterals', 'LexTokens', 'LexIgnore', 'LexRule', 'LexError',
          'YaccPrecedence', 'YaccTS', 'YaccRule',
          'CodeAll']
states = (('StateLex', 'exclusive'), 
          ('StateYacc', 'exclusive'),
          ('StateCode', 'exclusive'))

def t_ANY_LexBegin(t):
    r'%%\ *\t*LEX'
    t.lexer.begin('StateLex')
    return t

def t_StateLex_LexLiterals(t):
    r'%literals\ *=\ *\".*\"'
    t.value = t.value[1:]
    return t

def t_StateLex_LexTokens(t):
    r'%tokens\ *=\ *\[.*\]'
    t.value = t.value[1:]
    return t

def t_StateLex_LexIgnore(t):
    r'%ignore\ *=\ *\".*\"'
    t.value = t.value[1:]
    return t

def t_StateLex_LexRule(t):
    r'r\'.*\'\ *\t*return\(.*\)'
    return t

def t_StateLex_LexError(t):
    r'r\'.*\'\ *\t*error\(.*\)'
    return t

def t_ANY_YaccBegin(t):
    r'%%\ *\t*YACC'
    t.lexer.begin('StateYacc')
    return t

def t_StateYacc_YaccPrecedence(t):
    r'%precedence\ *=\ *\[.*\]'
    t.value = t.value[1:]
    return t

def t_StateYacc_YaccTS(t):
    r'ts\ *=\ *\{.*\}'
    return t

def t_StateYacc_YaccRule(t):
    r'\w+\ *\t*:\ *\t*.*{.*}'
    return t

def t_ANY_CodeBegin(t):
    r'%%\ *\t*'
    t.lexer.begin('StateCode')
    return t

def t_StateCode_CodeAll(t):
    r'.+'
    return t

def t_ANY_Str(t):
    r'[A-Za-z_]+'
    return t

def t_ANY_Int(t):
    r'\d+'
    return t

def t_ANY_Float(t):
    r'\d+.\d+'
    return t

def t_ANY_LPAR(t):         r'\(' ; return t
def t_ANY_RPAR(t):         r'\)' ; return t
def t_ANY_LSPAR(t):        r'\[' ; return t
def t_ANY_RSPAR(t):        r'\]' ; return t
def t_ANY_LCHAV(t):        r'{'  ; return t
def t_ANY_RCHAV(t):        r'}'  ; return t
def t_ANY_LESS(t):         r'<'  ; return t
def t_ANY_MORE(t):         r'>'  ; return t
def t_ANY_EQ(t):           r'='  ; return t
def t_ANY_PLUS(t):         r'\+' ; return t
def t_ANY_MINUS(t):        r'-'  ; return t
def t_ANY_TIMES(t):        r'\*' ; return t
def t_ANY_SLASH(t):        r'/'  ; return t
def t_ANY_BSLASH(t):       r'\\' ; return t
def t_ANY_PERC(t):         r'%'  ; return t
def t_ANY_QUOTE(t):        r'\"' ; return t
def t_ANY_PELICA(t):       r'\'' ; return t
def t_ANY_UNDERSCORE(t):   r'_'  ; return t
def t_ANY_DOT(t):          r'\.' ; return t
def t_ANY_COMMA(t):        r','  ; return t

def t_ANY_error(t):
    print("Illegal character '%s'" % t.value[0])
    t.lexer.skip(1)

t_StateLex_ignore = "\t \n"
t_StateYacc_ignore = "\t \n"
t_StateCode_ignore = "\n"
t_ignore = "\t \n"


lexer = lex()

#lexer.input(sys.stdin.read())
#for tok in lexer:
#    print(tok)

ts = { }

def p_Prog(p):
    "Prog : LexBegin Lexer YaccBegin Yacc CodeBegin Code"
    p[0]  = "\n# LEXER\n\n"
    p[0] += p[2]
    p[0] += "\n# YACC\n\n"
    p[0] += p[4]
    p[0] += "\n# RAW PYTHON\n\n"
    p[0] += p[6]

# :::::::::::::::::: Lex :::::::::::::::::

def p_Lexer(p):
    "Lexer : LexLits LexIgnore LexTokens LexRules LexErr"
    p[0] = f"{p[1]}\n{p[3]}\n\nt_{p[2]}\n\n{p[4]}\n{p[5]}\n"

# AJEITAR LITERALS
def p_LexLits_1(p): 
    "LexLits : LexLiterals"
    lits = re.match(r'\w+\ *\t*=\ *\t*\"(.*)\"', p[1])
    p[0] = "literals = "
    p[0] += '['
    for c in lits[1]:
        p[0]+= f"'{c}', "
    p[0] = p[0][:-2]
    p[0] += ']'

def p_LexLits_2(p): 
    "LexLits : "
    p[0] = "literals = []"

def p_LexRules_1(p):
    "LexRules : LexRules LexRule"
    p[0] = p[1]
    params = re.match(r'(r\'.*\')\ *\t*return\(\"(\w+)\",(.*)\)', p[2])
    p[0] += f"""def t_{params[2]}(t):
    {params[1]}
    return {params[3]}
"""
def p_LexRules_2(p):
    "LexRules : LexRule"
    params = re.match(r'(r\'.*\')\ *\t*return\(\"(\w+)\",(.*)\)', p[1])
    p[0] = f"""def t_{params[2]}(t):
    {params[1]}
    return {params[3]}
"""

def p_LexErr(p):
    "LexErr : LexError"
    params = re.match(r'(r\'.*\')\ *\t*error\((.*)\)', p[1])
    p[0] = "def t_error(t):\n"
    l = splitByMarks(params[2])
    for arg in l:
        while arg[0] == ' ':
            arg = arg[1:]
        p[0] += f"    {arg}\n"

# ::::::::::::::::: Yacc :::::::::::::::::

def p_Yacc(p):
    "Yacc : YaccPrec YaccTSym YaccRules"
    p[0] = f"{p[1]}\n{p[2]}\n\n{p[3]}\n"

def p_YaccPrec_1(p): "YaccPrec : YaccPrecedence" ; p[0] = p[1]
def p_YaccPrec_2(p): "YaccPrec : "               ; p[0] = ""

def p_YaccTSym_1(p): "YaccTSym : YaccTS"         ; p[0] = p[1]
def p_YaccTSym_2(p): "YaccTSym : "               ; p[0] = ""

def p_YaccRules_1(p):
    "YaccRules : YaccRules YaccRule"
    p[0] = p[1]
    params = re.match(r'(\w+)\ *\t*:\ *\t*(.*)\{(.*)\}', p[2])
    if params[1] in ts:
        ts[params[1]] = ts[params[1]] + 1
    else:
        ts[params[1]] = 1
    inst = params[3]
    while inst and inst[0] == ' ':
        inst = inst[1:]
    p[0] += f"""def p_{params[1]}_{ts[params[1]]}(t):
    \"{params[1]} : {params[2]}\"
    {inst}
"""

def p_YaccRules_2(p):
    "YaccRules : YaccRule"
    params = re.match(r'(\w+)\ *\t*:\ *\t*(.*)\{(.*)\}', p[1])
    if params[1] in ts:
        ts[params[1]] = ts[params[1]] + 1
    else:
        ts[params[1]] = 1
    inst = params[3]
    while inst and inst[0] == ' ':
        inst = inst[1:]
    p[0] = f"""def p_{params[1]}_{ts[params[1]]}(t):
    \"{params[1]} : {params[2]}\"
    {inst}
"""

# ::::::::::::::::: Code :::::::::::::::::

def p_Code_1(p): "Code : Code CodeAll" ; p[0] = f"{p[1]}\n{p[2]}"
def p_Code_2(p): "Code : CodeAll"      ; p[0] = p[1]

def p_error(p):
    print(f"Syntax error ", p)
    parser.success = False


# ::::::::::::::::: AUX :::::::::::::::::

def splitByMarks(s):
    lst = list()
    init_mark = { '(' : 0 , '[' : 1 , '{' : 2 , '\'' : 3 , '\"' : 4 }
    end_mark  = { 0 : ')' , 1 : ']' , 2 : '}' , 3 : '\'' , 4 : '\"' }
    last_bracket = ''
    index = -1
    word = ""
    closing = False
    for c in s:
        if c in init_mark and last_bracket not in init_mark:
            last_bracket = c
            index = init_mark[c]
            closing = False
        elif c in end_mark.values() and end_mark[index] == c:
            last_bracket = end_mark[index]
            closing = True
        if c == ',' and last_bracket in end_mark.values() and closing:
            lst.append(word)
            word = ""
            continue
        elif c == ',' and last_bracket in init_mark:
            word += c
            continue
        elif c == ',':
            lst.append(word)
            word = ""
            continue
        word += c
    lst.append(word)
    return lst

# :::::::::::::::::::::::::::::::::::::::


parser = yacc()

parser.success = True
codigo = parser.parse(sys.stdin.read())

if parser.success:
    print(codigo)
else:
    print("Programa com erros. Corrige e tente novamente...")