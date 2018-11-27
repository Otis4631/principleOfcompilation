
class Symbol():
    def __init__(self, text):
        self.text = text

    def match(self, symbol):
        if self.text == "None":
            if isinstance(symbol, Token):
                return False
        if not isinstance(symbol, Symbol):
            return False

        return self.text == symbol.text

    def __repr__(self):
        return str("" + str(self.text))


class Token(Symbol):
    def __init__(self, token, text=None, prop=0):
        super(Token, self).__init__(text)
        self.token = token
        self.text = text
        self.prop = prop

    def __repr__(self):
        return str(self.token + " " + self.text)

    def match(self, token):
        """
        检查输入的token是否与本token匹配（name，text）
        :param tokoen:
        :return:
        """
        if not isinstance(token, Token):
            return False
        # print(self.token, token.token)
        return self.token == token.token


class TokenException(Exception):
    """源代码分割token出错，抛出异常"""
    def __init__(self, bad_part):
        self.bad_part = bad_part
    def __str__(self):
        return "Error lexing part: " + self.bad_part

#双目比较
equal_comp = Token("equal_comp", "==")
noteq_comp = Token("noteq_comp", "!=")
lesseq_comp = Token("lesseq_comp", "<=")
greateq_comp = Token("greateq_comp", ">=")

#与非
logic_and = Token("logic_and", "&&", 65)
logic_or = Token("logic_or", "||", 60)

#单目运算符及界符
left_curly_bracket = Token("left_curly_bracket", "{")
right_curly_bracket = Token("right_curly_bracket", "}")
left_bracket = Token("left_bracket", "(", 100)
right_bracket = Token("right_bracket", ")")
left_sq_bracket = Token("left_sq_bracket", "[", 100)
right_sq_bracket = Token("right_sq_bracket", "]")
equal = Token("op_as", "=", 50)
less_comp = Token("less_comp", "<", 75)
great_comp = Token("great_comp", ">", 75)
semicolon = Token("semicolon", ";")
comma = Token("comma", ",")
minus = Token("minus", "-", 85)
plus = Token("op_add", "+", 85)
aster = Token("op_mul", "*", 90)
amper = Token("amper", "&", 95)
slash = Token("slash", "/", 90)
percent = Token("percent", "%", 90)
logic_not = Token("logic_not", "!", 95)

#关键字
if_keyword = Token("if_keyword", "if")
else_keyword = Token("else_keyword", "else", 210)
break_keyword = Token("break_keyword", "break")
cont_keyword = Token("cont_keyword", "continue")
while_keyword = Token("while_keyword", "while")
for_keyword = Token("for_keyword", "for")
return_keyword = Token("return_keyword", "return")
print_command = Token("print_command", "print")
int_keyword = Token("int_keyword", "int")
main_keyword = Token("main_keyword", 'main')


Tokens = [
    minus,
    plus,
    aster,
    equal,
    left_bracket,
    right_bracket,

]
id_str = [id.text for id in Tokens]

#token字典  token.text：token
token_dict = dict(zip(id_str, Tokens))