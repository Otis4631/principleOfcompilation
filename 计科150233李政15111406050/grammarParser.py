from grammar_v2 import grams_dict as grammars

def grammar_parser(start_symbol, token_steam, ):
    symbol_stack = []
    token_stack = token_steam
    tree_stack = []

    while True:
        for s in grammars:
                a = grammars[s]
                rule = grammars[s]
                rule = a
                if len(rule.gram_right) > len(symbol_stack):
                    continue
                else:
                    for rule_el, stack_el in zip(reversed(rule.gram_right), reversed(symbol_stack)):

                        if not rule_el.match(stack_el):
                            break
                    else:
                        if len(rule.gram_right) == 1:
                            symbol_stack.pop()
                            symbol_stack.append(rule.gram_left)
                        else:
                            symbol_stack[-len(rule.gram_right):] = rule.gram_left

                        print("\t", "rule:", rule)
                        print(symbol_stack , "     |     " , token_stack)
                        break
        else:
            if not token_stack:
                break
            else:
                symbol_stack.append(token_stack[0])
                if token_stack[0] == 'i':

                token_stack = token_stack[1:]
                print(symbol_stack , "     |     ", token_stack)
    if symbol_stack == [start_symbol]:
        print("True")
    else:
        print("False")
