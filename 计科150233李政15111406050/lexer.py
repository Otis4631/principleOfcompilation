import re
from Tokens import *
def lexer(program):
#     print(
#         """{}
# Program need to be lexed:
# {}\n{}
#         """.format("*" * 30, program, "*" * 30)
#     )
    """
    词法分析器

    :return:
    """
    keyword = ["if", "main", " if", "else", "for", "while", "int", 'return']

    boundary = ['{', '}', '(', ')', ',', ';']

    operator = ['=', '+', '-', '*', '/', '<', '>', '!']
    ans = []
    program_length = len(program)
    i = 0
    while i < program_length:
        if program[i].isalpha():
            j = i + 1
            try:
                while program[j].isalpha() or program[j].isdigit(): j += 1
            except IndexError:
                pass
            if program[i:j] in keyword:
                ans.append(token_dict[program[i:j]])
            else:
                ans.append(Token('i', program[i:j]))
            i = j
        elif program[i].isdigit():
            j = i + 1
            try:
                while program[j].isdigit(): j += 1
            except IndexError:
                pass
            ans.append(Token("number", program[i:j]))
            i = j
        elif program[i] in operator:
            if program[i + 1] in operator:
                ans.append(token_dict[program[i, i + 2]])
                i += 2
            else:
                ans.append(token_dict[program[i]])
                i += 1
        elif program[i] in boundary:
            ans.append(token_dict[program[i]])
            i += 1
        else:
            i += 1
    ans.append(Token("#", "#"))
    return ans





