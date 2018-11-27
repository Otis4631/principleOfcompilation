# E → i = E
# E → E + T | T
# T → T * F | F
# F → i | (E)


# E - TG
# E - i=E
# G - +TG | &
# T - FH
# H - *FH | &
# F - i | (E)


from grammar_v2 import Grammar, Symbol
E = Symbol("E")
G = Symbol("G")
T = Symbol("T")
H = Symbol("H")
F = Symbol("F")
ans = []
index = 0


def parser(token_steam):

    def fun_H():
        global index
        if token_steam[index].token == "op_mul":
            index += 1
            ans.append(Grammar(H, ["*", F, H]))
            fun_F()
            fun_H()
        else:
            ans.append(Grammar(H, ["&"]))


    def fun_F():
        global index
        if token_steam[index].token == "i":
            index += 1
            ans.append(Grammar(F, ["i"]))
        elif token_steam[index].token == "left_bracket":
            index += 1
            ans.append(Grammar(F, ['(', 'E', ')']))
            fun_E()
            if not token_steam[index].token == "right_bracket":
                raise Exception
            else:
                index += 1
        else:
            raise Exception



    def fun_G():
        global index
        if token_steam[index].token == 'op_add':
            index += 1
            ans.append(Grammar(G, ["+", T, G]))
            fun_T()
            fun_G()
        else:
            ans.append(Grammar(G, ["&"]))

    def fun_T():
        ans.append(Grammar(T, [F, H]))
        fun_F()
        fun_H()

    def fun_E():
        global index
        if token_steam[index].token == "i":
            index += 1
            if token_steam[index].token == "op_as":
                index += 1
                ans.append(Grammar(E, ["i", "=", E]))
                fun_E()
            else:
                index -= 1
                ans.append(Grammar(E, [T, G]))
                fun_T()
                fun_G()
        else:
            ans.append(Grammar(E, [T, G]))
            fun_T()
            fun_G()
    try:
        fun_E()
    except Exception as err:
        print(err)
        return ans, False, index

    if index == len(token_steam) - 1:
        return ans, True, index


