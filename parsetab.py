
# parsetab.py
# This file is automatically generated. Do not edit.
# pylint: disable=W,C,R
_tabversion = '3.10'

_lr_method = 'LALR'

_lr_signature = 'BACKSLASH CHAVSTXT COMMA DDOT DEF DIVIDE DOT EQUALS ERROR IGNORE INDEX LBRAC LCHAV LEX LIST LITERALS LRBRAC MINUS NUMBER PELICA PERC PLUS PRECEDENCE QUOTE RBRAC RCHAV REGEX RETURN RRBRAC SSTR STR TIMES TOKENS TS YACCPROG : LEXER GRAM CODECODE : CODE FUNCTIONSCODE : CODE ARGSCODE : FUNCTIONSCODE : ARGSFUNCTIONS : FUNCTIONS FUNCTIONFUNCTIONS : FUNCTIONFUNCTION : DEF STR LBRAC STR RBRAC DDOTLEXER : LIT IGN TOK TRULESIGN : PERC IGNORE EQUALS SSTRLIT : PERC LITERALS EQUALS SSTRTOK : PERC TOKENS EQUALS LISTTRULES : TRULE TRULESTRULES : TERRTRULE : REGEX RETURN LBRAC SSTR COMMA ARGS RBRACTERR : REGEX ERROR LBRAC INSTS RBRACINSTS : ARGS COMMA ARGSARGS : ARGS COMMA ARGSARGS : ARGS ARGSARGS : ARGS DOT ARGSARGS : ARGS LBRAC ARGS RBRACARGS : ARGS EQUALS ARGSARGS : ARGS PLUS ARGSARGS : ARGS MINUS ARGSARGS : ARGS TIMES ARGSARGS : ARGS DIVIDE ARGSARGS : ARGARG : STRARG : NUMBERARG : LISTARG : INDEXARG : SSTRARG : CHAVSTXTGRAM : PRCDNC TSYM GRULESTSYM : TS EQUALS CHAVSTXTPRCDNC : PERC PRECEDENCE EQUALS LISTGRULES : GRULES GRULE GRULES : GRULE GRULE : STR DDOT PARAMS CHAVSTXTPARAMS : PARAMS PARAMPARAMS : PARAMPARAM : STRPARAM : PELICA SYM PELICASYM : EQUALSSYM : PLUSSYM : MINUSSYM : TIMESSYM : DIVIDE'
    
_lr_action_items = {'PERC':([0,2,3,8,48,50,54,68,72,97,],[4,7,9,27,-9,-14,-11,-13,-10,-16,]),'$end':([1,11,12,13,14,15,17,18,19,20,21,22,30,31,32,33,55,56,58,59,60,61,62,73,94,],[0,-1,-4,-5,-7,-27,-28,-29,-30,-31,-32,-33,-2,-3,-6,-19,-18,-20,-22,-23,-24,-25,-26,-21,-8,]),'LITERALS':([4,],[10,]),'DEF':([5,11,12,13,14,15,17,18,19,20,21,22,30,31,32,33,43,44,55,56,58,59,60,61,62,64,73,83,94,],[16,16,16,-5,-7,-27,-28,-29,-30,-31,-32,-33,16,-3,-6,-19,-34,-38,-18,-20,-22,-23,-24,-25,-26,-37,-21,-39,-8,]),'STR':([5,11,12,13,14,15,16,17,18,19,20,21,22,23,30,31,32,33,34,35,36,37,38,39,40,41,43,44,55,56,57,58,59,60,61,62,63,64,65,66,73,75,76,77,80,83,84,93,94,95,96,98,99,100,],[17,17,-4,17,-7,-27,42,-28,-29,-30,-31,-32,-33,45,-2,17,-6,17,17,17,17,17,17,17,17,17,45,-38,17,17,17,17,17,17,17,17,74,-37,75,-35,-21,-42,75,-41,17,-39,-40,17,-8,-43,17,17,17,17,]),'NUMBER':([5,11,12,13,14,15,17,18,19,20,21,22,30,31,32,33,34,35,36,37,38,39,40,41,43,44,55,56,57,58,59,60,61,62,64,73,80,83,93,94,96,98,99,100,],[18,18,-4,18,-7,-27,-28,-29,-30,-31,-32,-33,-2,18,-6,18,18,18,18,18,18,18,18,18,-34,-38,18,18,18,18,18,18,18,18,-37,-21,18,-39,18,-8,18,18,18,18,]),'LIST':([5,11,12,13,14,15,17,18,19,20,21,22,30,31,32,33,34,35,36,37,38,39,40,41,43,44,47,55,56,57,58,59,60,61,62,64,71,73,80,83,93,94,96,98,99,100,],[19,19,-4,19,-7,-27,-28,-29,-30,-31,-32,-33,-2,19,-6,19,19,19,19,19,19,19,19,19,-34,-38,67,19,19,19,19,19,19,19,19,-37,81,-21,19,-39,19,-8,19,19,19,19,]),'INDEX':([5,11,12,13,14,15,17,18,19,20,21,22,30,31,32,33,34,35,36,37,38,39,40,41,43,44,55,56,57,58,59,60,61,62,64,73,80,83,93,94,96,98,99,100,],[20,20,-4,20,-7,-27,-28,-29,-30,-31,-32,-33,-2,20,-6,20,20,20,20,20,20,20,20,20,-34,-38,20,20,20,20,20,20,20,20,-37,-21,20,-39,20,-8,20,20,20,20,]),'SSTR':([5,11,12,13,14,15,17,18,19,20,21,22,29,30,31,32,33,34,35,36,37,38,39,40,41,43,44,53,55,56,57,58,59,60,61,62,64,73,79,80,83,93,94,96,98,99,100,],[21,21,-4,21,-7,-27,-28,-29,-30,-31,-32,-33,54,-2,21,-6,21,21,21,21,21,21,21,21,21,-34,-38,72,21,21,21,21,21,21,21,21,-37,-21,91,21,-39,21,-8,21,21,21,21,]),'CHAVSTXT':([5,11,12,13,14,15,17,18,19,20,21,22,30,31,32,33,34,35,36,37,38,39,40,41,43,44,46,55,56,57,58,59,60,61,62,64,73,75,76,77,80,83,84,93,94,95,96,98,99,100,],[22,22,-4,22,-7,-27,-28,-29,-30,-31,-32,-33,-2,22,-6,22,22,22,22,22,22,22,22,22,-34,-38,66,22,22,22,22,22,22,22,22,-37,-21,-42,83,-41,22,-39,-40,22,-8,-43,22,22,22,22,]),'TS':([6,67,],[24,-36,]),'PRECEDENCE':([7,],[25,]),'IGNORE':([9,],[28,]),'EQUALS':([10,13,15,17,18,19,20,21,22,24,25,28,31,33,52,55,56,57,58,59,60,61,62,73,78,93,99,100,],[29,37,-27,-28,-29,-30,-31,-32,-33,46,47,53,37,37,71,37,37,37,37,37,37,37,37,-21,86,37,37,37,]),'COMMA':([13,15,17,18,19,20,21,22,31,33,55,56,57,58,59,60,61,62,73,91,93,99,100,],[34,-27,-28,-29,-30,-31,-32,-33,34,34,34,34,34,34,34,34,34,34,-21,96,98,34,34,]),'DOT':([13,15,17,18,19,20,21,22,31,33,55,56,57,58,59,60,61,62,73,93,99,100,],[35,-27,-28,-29,-30,-31,-32,-33,35,35,35,35,35,35,35,35,35,35,-21,35,35,35,]),'LBRAC':([13,15,17,18,19,20,21,22,31,33,42,55,56,57,58,59,60,61,62,69,70,73,93,99,100,],[36,-27,-28,-29,-30,-31,-32,-33,36,36,63,36,36,36,36,36,36,36,36,79,80,-21,36,36,36,]),'PLUS':([13,15,17,18,19,20,21,22,31,33,55,56,57,58,59,60,61,62,73,78,93,99,100,],[38,-27,-28,-29,-30,-31,-32,-33,38,38,38,38,38,38,38,38,38,38,-21,87,38,38,38,]),'MINUS':([13,15,17,18,19,20,21,22,31,33,55,56,57,58,59,60,61,62,73,78,93,99,100,],[39,-27,-28,-29,-30,-31,-32,-33,39,39,39,39,39,39,39,39,39,39,-21,88,39,39,39,]),'TIMES':([13,15,17,18,19,20,21,22,31,33,55,56,57,58,59,60,61,62,73,78,93,99,100,],[40,-27,-28,-29,-30,-31,-32,-33,40,40,40,40,40,40,40,40,40,40,-21,89,40,40,40,]),'DIVIDE':([13,15,17,18,19,20,21,22,31,33,55,56,57,58,59,60,61,62,73,78,93,99,100,],[41,-27,-28,-29,-30,-31,-32,-33,41,41,41,41,41,41,41,41,41,41,-21,90,41,41,41,]),'RBRAC':([15,17,18,19,20,21,22,33,55,56,57,58,59,60,61,62,73,74,92,99,100,],[-27,-28,-29,-30,-31,-32,-33,-19,-18,-20,73,-22,-23,-24,-25,-26,-21,82,97,101,-17,]),'REGEX':([26,49,81,101,],[51,51,-12,-15,]),'TOKENS':([27,],[52,]),'DDOT':([45,82,],[65,94,]),'RETURN':([51,],[69,]),'ERROR':([51,],[70,]),'PELICA':([65,75,76,77,84,85,86,87,88,89,90,95,],[78,-42,78,-41,-40,95,-44,-45,-46,-47,-48,-43,]),}

_lr_action = {}
for _k, _v in _lr_action_items.items():
   for _x,_y in zip(_v[0],_v[1]):
      if not _x in _lr_action:  _lr_action[_x] = {}
      _lr_action[_x][_k] = _y
del _lr_action_items

_lr_goto_items = {'PROG':([0,],[1,]),'LEXER':([0,],[2,]),'LIT':([0,],[3,]),'GRAM':([2,],[5,]),'PRCDNC':([2,],[6,]),'IGN':([3,],[8,]),'CODE':([5,],[11,]),'FUNCTIONS':([5,11,],[12,30,]),'ARGS':([5,11,13,31,33,34,35,36,37,38,39,40,41,55,56,57,58,59,60,61,62,80,93,96,98,99,100,],[13,31,33,33,33,55,56,57,58,59,60,61,62,33,33,33,33,33,33,33,33,93,33,99,100,33,33,]),'FUNCTION':([5,11,12,30,],[14,14,32,32,]),'ARG':([5,11,13,31,33,34,35,36,37,38,39,40,41,55,56,57,58,59,60,61,62,80,93,96,98,99,100,],[15,15,15,15,15,15,15,15,15,15,15,15,15,15,15,15,15,15,15,15,15,15,15,15,15,15,15,]),'TSYM':([6,],[23,]),'TOK':([8,],[26,]),'GRULES':([23,],[43,]),'GRULE':([23,43,],[44,64,]),'TRULES':([26,49,],[48,68,]),'TRULE':([26,49,],[49,49,]),'TERR':([26,49,],[50,50,]),'PARAMS':([65,],[76,]),'PARAM':([65,76,],[77,84,]),'SYM':([78,],[85,]),'INSTS':([80,],[92,]),}

_lr_goto = {}
for _k, _v in _lr_goto_items.items():
   for _x, _y in zip(_v[0], _v[1]):
       if not _x in _lr_goto: _lr_goto[_x] = {}
       _lr_goto[_x][_k] = _y
del _lr_goto_items
_lr_productions = [
  ("S' -> PROG","S'",1,None,None,None),
  ('PROG -> LEXER GRAM CODE','PROG',3,'p_PROG','compilador.py',80),
  ('CODE -> CODE FUNCTIONS','CODE',2,'p_CODE_1','compilador.py',86),
  ('CODE -> CODE ARGS','CODE',2,'p_CODE_2','compilador.py',87),
  ('CODE -> FUNCTIONS','CODE',1,'p_CODE_3','compilador.py',88),
  ('CODE -> ARGS','CODE',1,'p_CODE_4','compilador.py',89),
  ('FUNCTIONS -> FUNCTIONS FUNCTION','FUNCTIONS',2,'p_FUNCTIONS_1','compilador.py',91),
  ('FUNCTIONS -> FUNCTION','FUNCTIONS',1,'p_FUNCTIONS_2','compilador.py',94),
  ('FUNCTION -> DEF STR LBRAC STR RBRAC DDOT','FUNCTION',6,'p_FUNCTION_1','compilador.py',98),
  ('LEXER -> LIT IGN TOK TRULES','LEXER',4,'p_LEXER','compilador.py',102),
  ('IGN -> PERC IGNORE EQUALS SSTR','IGN',4,'p_IGN','compilador.py',110),
  ('LIT -> PERC LITERALS EQUALS SSTR','LIT',4,'p_LIT','compilador.py',114),
  ('TOK -> PERC TOKENS EQUALS LIST','TOK',4,'p_TOK','compilador.py',122),
  ('TRULES -> TRULE TRULES','TRULES',2,'p_TRULES_1','compilador.py',127),
  ('TRULES -> TERR','TRULES',1,'p_TRULES_2','compilador.py',128),
  ('TRULE -> REGEX RETURN LBRAC SSTR COMMA ARGS RBRAC','TRULE',7,'p_TRULE_1','compilador.py',130),
  ('TERR -> REGEX ERROR LBRAC INSTS RBRAC','TERR',5,'p_TERR_1','compilador.py',139),
  ('INSTS -> ARGS COMMA ARGS','INSTS',3,'p_INSTS_1','compilador.py',146),
  ('ARGS -> ARGS COMMA ARGS','ARGS',3,'p_ARGS_1','compilador.py',152),
  ('ARGS -> ARGS ARGS','ARGS',2,'p_ARGS_2','compilador.py',153),
  ('ARGS -> ARGS DOT ARGS','ARGS',3,'p_ARGS_3','compilador.py',154),
  ('ARGS -> ARGS LBRAC ARGS RBRAC','ARGS',4,'p_ARGS_4','compilador.py',155),
  ('ARGS -> ARGS EQUALS ARGS','ARGS',3,'p_ARGS_5','compilador.py',156),
  ('ARGS -> ARGS PLUS ARGS','ARGS',3,'p_ARGS_6','compilador.py',157),
  ('ARGS -> ARGS MINUS ARGS','ARGS',3,'p_ARGS_7','compilador.py',158),
  ('ARGS -> ARGS TIMES ARGS','ARGS',3,'p_ARGS_8','compilador.py',159),
  ('ARGS -> ARGS DIVIDE ARGS','ARGS',3,'p_ARGS_9','compilador.py',160),
  ('ARGS -> ARG','ARGS',1,'p_ARGS_10','compilador.py',161),
  ('ARG -> STR','ARG',1,'p_ARG_1','compilador.py',163),
  ('ARG -> NUMBER','ARG',1,'p_ARG_2','compilador.py',164),
  ('ARG -> LIST','ARG',1,'p_ARG_3','compilador.py',165),
  ('ARG -> INDEX','ARG',1,'p_ARG_4','compilador.py',166),
  ('ARG -> SSTR','ARG',1,'p_ARG_5','compilador.py',167),
  ('ARG -> CHAVSTXT','ARG',1,'p_ARG_6','compilador.py',168),
  ('GRAM -> PRCDNC TSYM GRULES','GRAM',3,'p_GRAM_1','compilador.py',170),
  ('TSYM -> TS EQUALS CHAVSTXT','TSYM',3,'p_TSYM_1','compilador.py',177),
  ('PRCDNC -> PERC PRECEDENCE EQUALS LIST','PRCDNC',4,'p_PRCDNC_1','compilador.py',181),
  ('GRULES -> GRULES GRULE','GRULES',2,'p_GRULES_1','compilador.py',185),
  ('GRULES -> GRULE','GRULES',1,'p_GRULES_2','compilador.py',186),
  ('GRULE -> STR DDOT PARAMS CHAVSTXT','GRULE',4,'p_GRULE_1','compilador.py',188),
  ('PARAMS -> PARAMS PARAM','PARAMS',2,'p_PARAMS_1','compilador.py',201),
  ('PARAMS -> PARAM','PARAMS',1,'p_PARAMS_2','compilador.py',202),
  ('PARAM -> STR','PARAM',1,'p_PARAM_1','compilador.py',204),
  ('PARAM -> PELICA SYM PELICA','PARAM',3,'p_PARAM_2','compilador.py',207),
  ('SYM -> EQUALS','SYM',1,'p_SYM_1','compilador.py',214),
  ('SYM -> PLUS','SYM',1,'p_SYM_2','compilador.py',215),
  ('SYM -> MINUS','SYM',1,'p_SYM_3','compilador.py',216),
  ('SYM -> TIMES','SYM',1,'p_SYM_4','compilador.py',217),
  ('SYM -> DIVIDE','SYM',1,'p_SYM_5','compilador.py',218),
]
