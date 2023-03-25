from stackArrayBased import Stack
def isValid(s):
    stack=Stack()
    input_parth='([{'
    match={'(': ')', '{': '}', '[' : ']'}

    for p in s:
        if p in input_parth:
            stack.push(p)
        else:

            if not stack.is_empty() and match[stack.top()] == p:
                stack.pop()

            else:
                return False
    return stack.is_empty()
if __name__ == "__main__":
    print(isValid("()"))
    print(isValid("()[]{}"))
    print(isValid("(]"))
    print(isValid("([)]"))
    print(isValid("{[]}"))