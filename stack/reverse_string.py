import stacks


def rev_string_using_stack(string):
    rev_str_st = stacks.Stack()
    # push all characters into stack.
    for c in string:
        rev_str_st.push(c)

    # Build a new reverse string and return it
    rev_str = ""
    while not rev_str_st.isEmpty():
        rev_str += rev_str_st.pop()
    return rev_str

print (rev_string_using_stack("ult pult"))
