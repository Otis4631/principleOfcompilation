import Tokens
from lexer import *

class Symbol:
    """
    C文法中的符号标志
    """
    def __init__(self, name):
        self.name = name
    def __repr__(self):
        return self.name
    def match(self, symbol):
        if not isinstance(symbol, Symbol):
            return False
        return (self.name == symbol.name)

class Rule:
    """
    c文法中的规则
    """
    def __init__(self, orig, new, pro = None):
        self.orig = orig
        self.new = new
    def __repr__(self):
        return str(self.orig) + " -> " + str(self.new)

S = Symbol("S")
main_setup = Symbol("main_setup")

statements = Symbol("statements") #语句的集合
statement = Symbol("statement") #语句
statements_return = Symbol("statements_return")

E = Symbol("E") #通用

#声明
declare_separator = Symbol("declare_separator")
declare_type = Symbol("declare_type")
declare_expression = Symbol("declare_expression")

#数组
arr_start = Symbol("arr_start")
arr_end = Symbol("arr_end")
arr_list = Symbol("arr_list")

#if
if_start = Symbol("if_start")
if_statement = Symbol("if_statement")
else_statement = Symbol("else_statement")

#while
while_start = Symbol("while_start")
while_statement = Symbol("while_statement")

#for
for_start = Symbol("for_start")
for1 = Symbol("for1")
for2 = Symbol("for2")
for3 = Symbol("for3")
for_expr =  Symbol("for_expr")

arg_start = Symbol("arg_start")
func_dec = Symbol("func_dec")
func_def = Symbol("func_def")
func_call_start = Symbol("func_call_start") #函数调用
return_form = Symbol("return_form")
"""
规约规则
"""

main_func_dec_cont = Rule(S, [S, func_dec])
main_func_def_cont = Rule(S, [S, func_def])
main_func_dec = Rule(S, [func_dec])
main_func_def = Rule(S, [func_def])

statements_cont = Rule(statements, [statements,
                                    statement])

statements_end = Rule(statements, [statement])

return_form = Rule(statement, [Tokens.return_command,
                               E,
                               Tokens.semicolon])

print_form = Rule(statement, [Tokens.print_command,
                              E,
                              Tokens.semicolon])

useless_declaration = Rule(statement, [Id("type"), Tokens.semicolon])

real_declaration = Rule(statement, [declare_expression, Tokens.semicolon])

declare_type_base = Rule(declare_type, [Id("type")])
declare_type_cont = Rule(declare_type, [declare_type, Tokens.aster])

declare_separator_base = Rule(declare_separator, [Tokens.comma])
declare_separator_cont = Rule(declare_separator, [declare_separator, Tokens.aster])

base_declare = Rule(declare_expression, [declare_type, Id("name")])
assign_declare = Rule(declare_expression, [declare_expression, Tokens.equal, E], 49)
arr_assign_declare = Rule(declare_expression, [declare_expression, Tokens.equal, arr_list], 49)

cont_declare = Rule(declare_expression, [declare_expression, declare_separator, Id("name")])


array_num_declare = Rule(declare_expression, [declare_expression,
                                              Tokens.open_sq_bracket,
                                              E,
                                              Tokens.close_sq_bracket])


array_nonum_declare = Rule(declare_expression, [declare_expression,
                                                Tokens.open_sq_bracket,
                                                Tokens.close_sq_bracket])
E_num = Rule(E, [Id("number")])
E_parens = Rule(E, [Tokens.open_paren,
                    E,
                    Tokens.close_paren])


E_add = Rule(E, [E,
                 Id("addop"),
                 E], 85)

E_mult = Rule(E, [E,
                  Tokens.aster,
                  E], 90)

E_div = Rule(E, [E, Tokens.slash, E], 90)

E_mod = Rule(E, [E,
                 Tokens.percent,
                 E], 90)

E_boolean_and = Rule(E, [E,
                         Tokens.logic_and,
                         E], 65)

E_boolean_or = Rule(E, [E,
                        Tokens.logic_or,
                        E], 60)

E_eq_compare = Rule(E, [E,
                        Id("eq_compare"),
                        E], 70)

E_compare = Rule(E, [E,
                     Id("compare"),
                     E], 75)


E_neg = Rule(E, [Id("addop"),
                 E], 95)



E_equal = Rule(E, [E,
                   Id("assignment"),
                   E], 49)


E_boolean_not = Rule(E, [Tokens.logic_not, E], 95)


E_inc_after = Rule(E, [E, Id("crement")], 100)
E_inc_before = Rule(E, [Id("crement"), E], 95)

E_point = Rule(E, [Tokens.aster, E], 95)
E_deref = Rule(E, [Tokens.amper, E], 95)


E_func_noarg = Rule(E, [E, Tokens.open_paren, Tokens.close_paren])

E_func_call_start = Rule(func_call_start, [E, Tokens.open_paren, E], 0)

E_func_call_cont = Rule(func_call_start, [func_call_start, Tokens.comma, E], 0)

E_func_call_end = Rule(E, [func_call_start, Tokens.close_paren])


E_array = Rule(E, [E, Tokens.open_sq_bracket, E, Tokens.close_sq_bracket], 100)

E_var = Rule(E, [Id("name")])

E_form = Rule(statement, [E, Tokens.semicolon])

if_start_form = Rule(if_start, [Tokens.if_keyword,
                                Tokens.open_paren])


if_form_brackets = Rule(if_statement, [if_start,
                                       E,
                                       Tokens.close_paren,
                                       Tokens.open_bracket,
                                       Tokens.close_bracket])


if_form_oneline = Rule(if_statement, [if_start,
                                      E,
                                      Tokens.close_paren,
                                      statements])


if_form_main = Rule(if_statement, [if_start,
                                   E,
                                   Tokens.close_paren,
                                   Tokens.open_bracket,
                                   statements,
                                   Tokens.close_bracket])


else_form_brackets = Rule(else_statement, [Tokens.else_keyword,
                                           Tokens.open_bracket,
                                           Tokens.close_bracket])

else_form_oneline = Rule(else_statement, [Tokens.else_keyword,
                                          statements])

else_form_main = Rule(else_statement, [Tokens.else_keyword,
                                       Tokens.open_bracket,
                                       statements,
                                       Tokens.close_bracket])


if_form_general = Rule(statement, [if_statement], 200)
ifelse_form_general = Rule(statement, [if_statement, else_statement])

break_form = Rule(statement, [Tokens.break_keyword, Tokens.semicolon])
cont_form = Rule(statement, [Tokens.cont_keyword, Tokens.semicolon])

while_start_form = Rule(while_start, [Tokens.while_keyword, Tokens.open_paren])


while_form_brackets = Rule(statement, [while_start,
                                       E,
                                       Tokens.close_paren,
                                       Tokens.open_bracket,
                                       Tokens.close_bracket])

while_form_oneline = Rule(statement, [while_start,
                                      E,
                                      Tokens.close_paren,
                                      statements])

while_form_main = Rule(statement, [while_start,
                                   E,
                                   Tokens.close_paren,
                                   Tokens.open_bracket,
                                   statements,
                                   Tokens.close_bracket])

for_start_form = Rule(for_start, [Tokens.for_keyword, Tokens.open_paren])
for1_form = Rule(for1, [for_start, statements])



for2_form = Rule(for2, [for1, statements])
for_expr_form = Rule(for_expr, [for2, E, Tokens.close_paren])
for_expr_form_empty = Rule(for_expr, [for2, Tokens.close_paren])


for_form_empty = Rule(statement, [for_expr,
                                  Tokens.semicolon])
for_form_brackets = Rule(statement, [for_expr,
                                     Tokens.open_bracket,
                                     Tokens.close_bracket])
for_form_oneline = Rule(statement, [for_expr,
                                    statements])
for_form_main = Rule(statement, [for_expr,
                                 Tokens.open_bracket,
                                 statements,
                                 Tokens.close_bracket])


arr_list_one = Rule(arr_list, [Tokens.open_bracket, E, Tokens.close_bracket])

arr_list_none = Rule(arr_list, [Tokens.open_bracket, Tokens.close_bracket])

arr_list_start = Rule(arr_start, [Tokens.open_bracket, E, Tokens.comma])

arr_list_cont = Rule(arr_start, [arr_start, E, Tokens.comma])

arr_list_total = Rule(arr_list, [arr_start, arr_end])

arr_list_end = Rule(arr_end, [E, Tokens.close_bracket])


base_arg_form = Rule(arg_start, [declare_expression,
                                 Tokens.open_paren,
                                 declare_expression])
cont_arg_form = Rule(arg_start, [arg_start,
                                 Tokens.comma,
                                 declare_expression])

func_dec_form = Rule(func_dec, [arg_start, Tokens.close_paren, Tokens.semicolon])
func_def_form = Rule(func_def, [arg_start,
                                Tokens.close_paren,
                                Tokens.open_bracket,
                                statements,
                                Tokens.close_bracket])

noarg_func_dec_form = Rule(func_dec, [declare_expression,
                                      Tokens.open_paren,
                                      Tokens.close_paren,
                                      Tokens.semicolon])
noarg_func_def_form = Rule(func_def, [declare_expression,
                                      Tokens.open_paren,
                                      Tokens.close_paren,
                                      Tokens.open_bracket,
                                      statements,
                                      Tokens.close_bracket])

semicolon_form = Rule(statement, [Tokens.semicolon])


rules = \
    [
         main_func_def_cont,
         main_func_dec_cont,
         main_func_def,
         main_func_dec,
         statements_cont,
         statements_end,
         return_form,
         print_form,

         useless_declaration,
         real_declaration,
         declare_type_base,
         declare_type_cont,
         declare_separator_base,
         declare_separator_cont,
         base_declare,
         assign_declare,
         arr_assign_declare,
         cont_declare,
         array_num_declare,
         array_nonum_declare,

         E_num,
         E_parens,
         E_add,
         E_mult,
         E_div,
         E_mod,
         E_boolean_and,
         E_boolean_or,
         E_eq_compare,
         E_compare,
         E_neg,
         E_equal,
         E_boolean_not,
         E_inc_after,
         E_inc_before,
         E_point,
         E_deref,
         E_func_noarg,
         E_func_call_start,
         E_func_call_cont,
         E_func_call_end,
         E_array,
         E_var,
         E_form,

         if_start_form,
         if_form_brackets,
         if_form_oneline,
         if_form_main,
         if_form_general,
         else_form_brackets,
         else_form_oneline,
         else_form_main,
         ifelse_form_general,

         break_form,
         cont_form,

         while_start_form,
         while_form_brackets,
         while_form_oneline,
         while_form_main,

         for_start_form,
         for1_form,
         for2_form,
         for_expr_form,
         for_expr_form_empty,
         for_form_brackets,
         for_form_oneline,
         for_form_main,

         arr_list_one,
         arr_list_none,
         arr_list_start,
         arr_list_cont,
         arr_list_total,
         arr_list_end,

         base_arg_form,
         cont_arg_form,
         func_dec_form,
         func_def_form,
         noarg_func_dec_form,
         noarg_func_def_form,

         semicolon_form
    ]
