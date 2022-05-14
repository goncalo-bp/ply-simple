from ply.lex import lex
from ply.yacc import yacc 
import sys
import re
import math

# ANALISADOR LÉXICO

reservadas = "ler print int while".split()
tokens = ['num','var'] + [x.upper() for x in reservadas]
literals = "( ) + - / * = ? : . ; ^ , { }".split()

t_ignore = " \t\n"

def t_var(t):
    r'[a-z]+'
    if t.value in reservadas:
        t.type = t.value.upper()
    return t

def t_num(t):
    r'\d+'
    t.value = int(t.value)
    return t

def t_error(t):
    r'.'
    print("Invalid character",t)
    t.lexer.skip(1)

lexer = lex()

# GRAMÁTICA


ts = {'last' : 0, 'loopc' : 0}

precedence = [
#              ('left',':'),
#              ('left','?'),
              ('left','+','-'),
#              ('left','*','/'),
#              ('right','^'),
              ('right','(')
              ]

def p_P_1(p): r"P : Decls Insts"         ; print(f'{p[1]}start\n{p[2]}\nstop\n')

def p_Decls_1(p): r"Decls : Decls Decl"  ; p[0] = p[1] + p[2]
def p_Decls_2(p): r"Decls : "            ; p[0] = ""

def p_Insts_1(p): r"Insts : Insts Inst"  ; p[0] = p[1] + p[2]
def p_Insts_2(p): r"Insts : "            ; p[0] = ""

def p_Decl_1(p): 
    r"Decl : INT Vars ';'"
    p[0] = p[2][0]
    for x in p[2][1]:
        ts[x] = (ts["last"] , p[1])
        ts["last"] += 1


def p_Vars_1(p): r"Vars : Vars ',' var"  ; p[0] = (f'{p[1][0]}pushi 0 // {p[3]}\n' , p[1][1] + [p[3]])
def p_Vars_2(p): r"Vars : var"           ; p[0] = (f'pushi 0 // {p[1]}\n' , [p[1]])

def p_Inst_1(p): r"Inst : var '=' Exp ';'" ; p[0] = f'{p[3]}storeg {ts[p[1]][0]}\n'
def p_Inst_2(p): r"Inst : PRINT Exp ';'"   ; p[0] = f'{p[2]}writei\n'
def p_Inst_3(p): r"Inst : '{' Insts '}'"   ; p[0] = p[2]
def p_Inst_4(p): 
    r"Inst : WHILE '(' Exp ')' Inst"
    p[0] = f'''while{ts["loopc"]}:
{p[3]}jz fimw{ts["loopc"]}
{p[5]}jump while{ts["loopc"]}
fimw{ts["loopc"]}:'''
    ts["loopc"] += 1


def p_Exp_1(p): "Exp : Exp '+' Exp"    ; p[0] = f'{p[1]}{p[3]}add\n'
def p_Exp_2(p): "Exp : Exp '-' Exp"    ; p[0] = f'{p[1]}{p[3]}sub\n'
def p_Exp_6(p): "Exp : '(' Exp ')'"    ; p[0] = p[2]
def p_Exp_7(p): "Exp : num"            ; p[0] = f'pushi {p[1]}\n'
def p_Exp_8(p): "Exp : var"            ; p[0] = f'pushg {ts[p[1]][0]}\n'
def p_Exp_12(p): "Exp : LER "          ; p[0] = "read\natoi\n"

def p_error(p):
    print("Erro sintático:", p)
    
parser = yacc()
# dá o output à medida que vamos colocando o input - experimentar descomentar estas duas linhas `
# for linha in sys.stdin:
# print(parser.parse(linha))

# só dá o output após ctrl D
parser.parse(sys.stdin.read())
