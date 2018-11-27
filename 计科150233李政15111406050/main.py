from lexer import lexer
from simple_parser import parser
from get_three_code import get_code
from Tokens import Symbol

def print_token(token_steam):
    print('#' * 50)
    print(token_steam)
    for t in token_steam:
        print("|%-20s|%20s|" % (t.token, t.text))

with open("1.c", "r") as fp:
    token_steam = lexer(fp.read())
    print_token(token_steam)
    ans, is_done, index = parser(token_steam)

    token = []
    var_table = []


    for i in token_steam:
        if i.token == 'i':
            var_table.append(i.text)

    for i in ans:
        for j in i.right:
            if isinstance(j, str):
                token.append(j)
    for i in range(len(ans)):
        for j in range(i + 1, len(ans) - 1):
            if ans[j].left == ans[i].left and ans[j].right == ans[i].right:
                ans.remove(ans[j])
                j -= 1
                i -= 1

    print(token)
    print(ans, is_done, end='\n')
    get_code(token, ans, Symbol('E'), var_table)