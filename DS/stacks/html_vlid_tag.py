from stackArrayBased import Stack
def isValid( code) :
    j=code.find("<")
    stack=Stack()
    while j !=-1:
        k = code.find(">" , j+1)
        if k==-1:
            return False
        cur_tag=code[j+1:k]
        if not cur_tag.startswith("/"):
            stack.push(cur_tag)
        else:
            if stack and cur_tag[1:] == stack.top():
                stack.pop()
            else:
                return False
        j=code.find("<" , k+1)
    return len(stack) == 0
if __name__ == "__main__":
    stack=Stack()
    code="<html><head><title>hello</title></head><body><h1>hello</h1></body></html>"
    print(isValid(code))
    code="<html><head></title>hello</title></head><body><h1>hello</h1></body></html>"
    print(isValid(code))
