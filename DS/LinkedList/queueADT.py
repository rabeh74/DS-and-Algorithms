class Queue:
    class _Node:
        __slots__ = "_val","_next"
        def __init__(self , val , next=None):
            self._val=val
            self._next=next

    def __init__(self, k: int):
        self._head=None
        self._tail=None
        self._capacity=k
        self._size=0

    def enQueue(self, value: int) -> bool:
        # print(self._size , self._capacity)
        if self._size == self._capacity:
            return False
        node = self._Node(value)
        if self._size != 0 :
            self._tail._next = node

        else:
            self._head=node

        self._tail=node
        self._size +=1
        return True


    def deQueue(self) -> bool:
        if self._size == 0:
            return False
        self._head=self._head._next
        self._size -=1
        if self._size ==0 :
            self._tail = None
            self._head=None

        return True

    def Front(self) -> int:
        if self._head:
            return self._head._val
        return -1


    def Rear(self) -> int:
        if self._tail:
            return self._tail._val
        return -1


    def isEmpty(self) -> bool:
        return self._size ==0

    def isFull(self) -> bool:
        return self._size == self._capacity

    def __len__(self):
        return self._size

if __name__ == '__main__':
    q=Queue(3)
    print(q.enQueue(1))
    print(q.enQueue(2))
    print(q.enQueue(3))
    print(q.enQueue(4))
    print(q.Rear())
    print(q.isFull())
    print(q.deQueue())
    print(q.enQueue(4))
    print(q.Rear())
    print(q.deQueue())
    print(q.deQueue())
    print(q.deQueue())
    print(q.deQueue())



