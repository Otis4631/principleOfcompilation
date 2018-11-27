from Tokens import *



class Grammar:
    def __init__(self, gram_left, gram_right):
        self.left = gram_left
        self.right = gram_right
        self.str_right = []
        for i in gram_right:
            if isinstance(i, Symbol):
                self.str_right.append(i.text)
            else:
                self.str_right.append(i)

    def __repr__(self):
        return str(str(self.left) + " --> " + str("".join(self.str_right)))


E = Symbol('E')



declare_alignment = Symbol("declare_alignment") #2
declare_statement = Symbol("declare_statement") #3


identifier_list = Symbol("identifier_list")#4
identifier = Token("var", "None")
number = Token("number", "None")


statement_alignment = Symbol("statement_alignment") #5
statement = Symbol("statement") #6
if_statement = Symbol("if_statement")
while_statement = Symbol("while_statement")
for_statement = Symbol("for_statement")
comp_statement = Symbol("comp_statement")
assign_statement = Symbol("assign_statement")
expression = Symbol("expression")
bool_expression = Symbol("bool_expression")
arith_expression = Symbol("arith_expression")
relational_op = Symbol("relational_op")
item = Symbol("item")
none = Symbol("None")
op = Symbol("op")
print_statement = Symbol("print_statement")
input_statement = Symbol("input_statement")
main = Symbol("main")

# termSet
# left_bracket = Symbol("left_bracket")
# right_bracket = Symbol("right_bracket")
# left_curly_bracket = Symbol("left_curly_bracket")
# right_curly_bracket = Symbol("right_curly_bracket")
# none = Symbol('none')
# comma = Symbol('comma')
# if_keyword = Symbol("if_keyword")
# while_keyword = Symbol('while_keyword')
# for_keyword = Symbol("for_keyword")
# else_keyword = Symbol("else_keyword")
# semicolon = Symbol("semicolon")
# equal = Symbol('equal')
# op = Symbol('op')
# add = Symbol('add')




##########

factor = Symbol("factor")

gram_main = Grammar(E, [main, left_bracket, right_bracket,
                        left_curly_bracket, declare_alignment, statement_alignment,
                        right_curly_bracket])

gram_main_k = Grammar(main, [main_keyword])


gram_declare_align_1 = Grammar(declare_alignment, [declare_alignment, declare_statement])
gram_declare_align_2 = Grammar(declare_alignment, [declare_statement])
gram_declare_align_3 = Grammar(declare_alignment, [none])


gram_declare_state = Grammar(int_keyword, [int_keyword, identifier_list])

gram_identifier_list_1 = Grammar(identifier_list, [identifier, comma, identifier_list])
gram_identifier_list_2 = Grammar(identifier_list, [identifier])

gram_state_align_1 = Grammar(statement_alignment, [statement_alignment, statement])
gram_state_align_2 = Grammar(statement_alignment, [statement])

gram_if_expr = Grammar(if_statement, [if_keyword, left_bracket, expression, right_bracket, comp_statement, semicolon])
gram_if_else_expr = Grammar(if_statement, [if_keyword, left_bracket, expression, right_bracket, comp_statement,
                                           else_keyword, comp_statement,semicolon])

gram_while_expr = Grammar(while_statement, [while_keyword, left_bracket,expression, right_bracket, comp_statement,semicolon])
gram_for_expr = Grammar(for_statement, [for_keyword, left_bracket, expression, semicolon,
                                        expression, semicolon, expression, right_bracket, comp_statement])
# 复合语句
gram_comp_state = Grammar(comp_statement, [left_curly_bracket, statement_alignment, right_curly_bracket])
# 赋值语句
gram_assign_state = Grammar(assign_statement, [expression, semicolon])

# 表达式
gram_expr_1 = Grammar(expression, [identifier, equal, arith_expression])
gram_expr_2 = Grammar(expression, [bool_expression])

# 布尔表达式
gram_bool_expr_1 = Grammar(bool_expression, [arith_expression])
gram_bool_expr_2 = Grammar(bool_expression, [arith_expression, op, arith_expression])

# 语句
gram_state_1 = Grammar(statement, [if_statement])
gram_state_2 = Grammar(statement, [for_statement])
gram_state_3 = Grammar(statement, [while_statement])
gram_state_4 = Grammar(statement, [comp_statement])
gram_state_5 = Grammar(statement, [assign_statement])
gram_state_6 = Grammar(statement, [print_statement])
gram_state_7 = Grammar(statement, [input_statement])

# 关系运算符
gram_op_1 = Grammar(op, [great_comp])
gram_op_2 = Grammar(op, [less_comp])
gram_op_3 = Grammar(op, [equal_comp])
gram_op_4 = Grammar(op, [lesseq_comp])
gram_op_5 = Grammar(op, [noteq_comp])
gram_op_6 = Grammar(op, [greateq_comp])

# 算数表达式
gram_arith_expr_1 = Grammar(arith_expression, [arith_expression, plus, item])
gram_arith_expr_2 = Grammar(arith_expression, [minus, item])
gram_arith_expr_3 = Grammar(arith_expression, [item])

# 项
gram_item_1 = Grammar(item, [item, aster, factor])
gram_item_2 = Grammar(item, [item, slash, factor])
gram_item_3 = Grammar(item, [factor])

# 因子
gram_factor_1 = Grammar(factor, [identifier])
gram_factor_2 = Grammar(factor, [number])
gram_factor_3 = Grammar(factor, [left_bracket, arith_expression, right_bracket])


grams ={}
grams = locals().copy()
grams_dict = {}
for gram in grams:
    if isinstance(grams[gram], Grammar):
        grams_dict[gram] = grams[gram]















