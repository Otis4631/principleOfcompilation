def get_code(token_steam, grammar_tree, start_symbol, var_table):
    symbol_stack = []
    token_stack = token_steam.copy()
    fmt_len = int(len(token_steam) * 4.5)
    print(fmt_len)
    min_table = []
    temp_var = 1
    ans = []
    pro = 0  # *:4 +:2 =:1
    pro += 4 if "*" in token_steam else 0
    pro += 2 if "+" in token_steam else 0
    pro += 1 if "=" in token_steam else 0

    while True:
        for rule in reversed(grammar_tree):
            if symbol_stack == [start_symbol, ]:
                break
            if len(rule.right) > len(symbol_stack):
                continue
            else:
                for rule_el, stack_el in zip(reversed(rule.right), reversed(symbol_stack)):
                    if isinstance(rule_el, str):
                        if rule_el != stack_el:
                            break
                    else:
                        if not rule_el.match(stack_el):
                            break
                else:
                    if len(rule.right) == 1:
                        if token_stack and token_stack[0] == "=":
                            pass
                        elif rule.left.text == "G":
                            if not symbol_stack[-2].text == 'T':
                                pass
                            else:
                                symbol_stack.pop()
                                symbol_stack.append(rule.left)
                                print("\t", "rule:", rule)

                        else:
                            symbol_stack.pop()

                            symbol_stack.append(rule.left)
                            print("%-{}s  |  %{}s".format(fmt_len, fmt_len + 2) % (str(symbol_stack), str(token_stack)))
                            print("\t", "rule:", rule)
                    else:
                        for i in range(len(rule.right)):
                            symbol_stack.pop()

                        symbol_stack.append(rule.left)

                        print("%-{}s  |  %{}s".format(fmt_len, fmt_len + 2) % (str(symbol_stack), str(token_stack)))
                        print("\t", "rule:", rule)
                        break
        else:
            if not token_stack:
                break
            else:
                symbol_stack.append(token_stack[0])
                if token_stack[0] == 'i':
                    min_table.append(var_table.pop())
                else:
                    min_table.append(token_stack[0])
                if pro == 7:
                    if "*" in min_table:
                        index = min_table.index('*')
                        if index != len(min_table) - 1:
                            s = "T{}={}{}{}".format(temp_var, min_table[index - 1], min_table[index], min_table[index + 1])
                            ans.append(s)
                            min_table[index - 1: index + 1] = ["T{}".format(temp_var)]
                            temp_var += 1
                            pro = 3
                elif pro == 3:
                    if "+" in min_table:
                        index = min_table.index('+')
                        if  index != len(min_table) - 1:
                            s = "T{}={}{}{}".format(temp_var, min_table[index - 1], min_table[index],
                                                    min_table[index + 1])
                            ans.append(s)
                            min_table[index - 1: index + 1] = ["T{}".format(temp_var)]
                            temp_var += 1
                            pro = 1
                elif pro == 1:
                    print(min_table)


                token_stack = token_stack[1:]
                print("%-{}s  |  %{}s".format(fmt_len, fmt_len + 2) % (str(symbol_stack), str(token_stack)))
    print("YES")