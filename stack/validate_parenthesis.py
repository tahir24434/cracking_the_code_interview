import stacks


def is_open_symbol(c):
    if c in "({[":
        return True


def is_closed_symbol(c):
    if c in ")}]":
        return True


def matches(open_sym, close_sym):
    opens = "({["
    closers = ")}]"
    return opens.index(open_sym) == closers.index(close_sym)


# Balanced parentheses means that each opening symbol has a corresponding closing symbol and the pairs of parentheses
# are properly nested.
# examples of balanced: (()()()()), (((()))), (()((())())), {{([][])}()}
# example of non_blncd: ((((((()), ())), (()()((), [{()]
def is_parentheses_balanced(symbol_string):
    open_par = stacks.Stack()
    for c in symbol_string:
        if is_open_symbol(c):
            open_par.push(c)
        elif is_closed_symbol(c):
            try:
                open_symbol = open_par.pop()
                if not matches(open_symbol, c):
                    return False
            except Exception:
                return False
    if open_par.isEmpty():
        return True
    else:
        return False

while 1:
    symbol_str = input()
    print (is_parentheses_balanced(symbol_str))