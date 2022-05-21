from ply.yacc import yacc
from ps_lex import tokens, literals, states


def p_PROG(p):
    "Prog : Lexer Gram Code"
    p[0] = "\nfrom ply.lex import lex\nfrom ply.yacc import yacc\n"
    p[0] += "\n# LEXER\n"
    p[0] += p[1]
    p[0] += "\n# YACC\n"
    p[0] += p[2]
    p[0] += "\n# PYTHON\n"
    p[0] += p[3]


def p_Lexer(p):
    "Lexer : Literals Ignore Tokens Trules"
    p[0] = f"""{p[1]}
{p[2]}
{p[3]}\n
{p[4]}
lexer = lex()
"""

def p_Literals(p): 
    "Literals : '%' LITERALS '=' SSTR"
    p[0] = f'literals = {p[4]}'
    p[4] = p[4][:-1]
    p[4] = p[4][1:]
    for x in p[4]:
        ts['ltls'].append(x)

def p_Ignore(p):
    "Ignore : '%' IGNORE '=' SSTR"
    p[0] = f't_ignore = {p[4]}'


def p_Tokens(p):
    "Tokens : '%' TOKENS '=' LIST"
    p[0] = f'tokens = {p[4]}'


def p_Trules_list(p): "Trules : Trule Trules"  ; p[0] = p[1] + p[2]
def p_Trules_err(p):  "Trules : Terr"          ; p[0] = p[1]

def p_Trule(p):
    "Trule : REGEX RETURN '(' SSTR ',' Args ')'"
    p[4] = p[4][1:]
    p[4] = p[4][:-1]
    p[0] = f"""def t_{p[4]}(t):
    {p[1]}
    t.value = {p[6]}
    return t
"""

def p_Terr(p):
    "Terr : REGEX ERROR '(' Insts ')'"
    p[0] = f"""def t_error(t):
    {p[1]}
    {p[4]}
"""

def p_Insts(p):
    "Insts : Arg ',' Arg"
    p[0] = f"""print({p[1]})
    {p[3]}
"""

def p_Args_list(p):   "Args : Args ',' Arg"           ;  p[0] = f"{p[1]}, {p[3]}"
def p_Args_single(p): "Args : Arg"                    ;  p[0] = p[1]

def p_Arg_str(p): "Arg : STR"           ; p[0] = p[1]
def p_Arg_func_str(p): "Arg : STR '(' STR ')'" ; p[0] = p[1] + p[2] + p[3] + p[4]
def p_Arg_func_number(p): "Arg : STR '(' NUMBER ')'" ; p[0] = p[1] + p[2] + str(p[3]) + p[4]
def p_Arg_sstr(p):  "Arg : SSTR"        ;   p[0] = p[1]


def p_Gram(p): 
    "Gram : Precedence SymbTab Grules"
    p[0] = f"""{p[1]}
{p[2]}
{p[3]}
"""


def p_Precedence(p):
    "Precedence : '%' PRECEDENCE '=' LIST"
    p[0] = f'precedence = {p[4]}\n'

def p_Precedence_empty(p):
    "Precedence : "
    p[0] = ""

def p_SymbTab(p):
    "SymbTab : TS '=' CHAVSTXT"
    p[0] = f"ts = {p[3]}\n"


def p_Grules_list(p):   "Grules : Grules Grule"  ;  p[0] = p[1] + p[2]
def p_Grule_single(p):  "Grules : Grule"         ;  p[0] = p[1]

def p_Grule(p):
    "Grule : STR ':' Params CHAVSTXT"
    p[4] = p[4][2:]
    p[4] = p[4][:-2]
    if p[1] in ts:
        ts[p[1]] = ts[p[1]] + 1
    else:
        ts[p[1]] = 1
    p[0] = f"""def p_{p[1]}_{ts[p[1]]}(t):
    \"{p[1]} : {p[3]}\"
    {p[4]}
"""

def p_Params_list(p):    "Params : Params Param" ; p[0] = f"{p[1]} {p[2]}"
def p_Params_single(p):  "Params : Param"        ; p[0] = f"{p[1]}"
def p_Params_empty(p):   "Params : "             ; p[0] = ""

def p_Param_str(p):
    "Param : STR"
    p[0] = p[1]

def p_Param_literal(p):
    "Param : LITERAL"

    # Tirar as plicas do LITERAL
    p[1] = p[1][1:]
    p[1] = p[1][:-1]

    if p[1] in ts['ltls']:
        # Caso exista, volta a colocar plicas e retorna
        p[0] = f"\'{p[1]}\'"
    else:
        # Retorna literal "vazio"
        p[0] = "\'\'"
        print(f"ERROR: Undefined literal '{p[1]}'")


def p_Param_prec(p):
    "Param : '%' STR"
    p[0] = p[1] + p[2]

def p_Code(p):     "Code : Code ALL" ; p[0] = f"{p[1]}\n{p[2]}"
def p_Code_all(p): "Code : ALL"      ; p[0] = p[1]


def p_error(p):
    print(f"Syntax error ", p)
    parser.success = False


# Build the parser
parser = yacc()
ts = {"ltls" : []}

# Read program from input and parse it
import sys
parser.success = True
codigo = parser.parse(sys.stdin.read())

if parser.success:
    print(codigo)
else:
    print("Programa com erros. Corrige e tente novamente...")