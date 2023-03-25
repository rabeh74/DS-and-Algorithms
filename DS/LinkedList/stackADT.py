class Stack:
    class _Node:
        # restrict the attributes of the class
        __slots__="_val","_next" # to save memory space and speed up the execution
        def __init__(self , val , next):
            self._val=val
            self._next=next

    def __init__(self):
        self._size=0
        self._head=None

    def push(self, val: int) -> None:
        self._head=self._Node(val , self._head)
        self._size +=1

    def pop(self) -> None:
        if self.is_empty():
            raise Exception("Stack is empty")
        val= self._head._val
        self._head=self._head._next
        self._size -=1
        return val

    def top(self) -> int:
        if not self._head:
            return None
        return self._head._val
    def __len__(self):
        return self._size

    def is_empty(self):
        return self._size==0
    def top(self):
        if self.is_empty():
            raise Exception("Stack is empty")
        return self._head._val



if __name__ == '__main__':
    s=Stack()
    print(s.is_empty())
    # True
    s.push(1)
    s.push(2)
    s.push(3)
    print(len(s))
    # 3
    print(s.pop())

    print(s.pop())
    # 2
    print(s.top())
    print(s.is_empty())
    print(s.pop())

    print(s.pop())
    # raise Exception("Stack is empty")
