class Empty(Exception):
    pass

class Stack:
    def __init__(self):
        self._data=[]

    def is_empty(self):
        return len(self._data)==0

    def push(self , val):
        self._data.append(val)

    def pop(self):
        if self.is_empty():
            raise Empty("stack is empty")
        return self._data.pop()

    def top(self):
        if self.is_empty():
            raise Empty("stack is empty")
        return self._data[-1]
    def __len__(self):
        return len(self._data)

if __name__ == "__main__":
    stack=Stack()
    stack.push(1)
    stack.push(2)
    stack.push(3)
    stack.push(4)
    print(stack.top())
    print(stack.pop())
    print(stack.top())
    print(stack.pop())
    print(len(stack))
    stack.pop()
    print(stack.is_empty())
    stack.pop()
    print(stack.is_empty())