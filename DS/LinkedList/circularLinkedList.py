"""
Round Robin Scheduling Algorithm

"""

class CircularQueue:
    class _Node:
        __slots__ = '_val', '_next'
        def __init__(self, val, next):
            self._val = val
            self._next = next

    def __init__(self):
        self._tail = None
        self._size = 0
        # head is self._tail._next

    def __len__(self):
        return self._size

    def is_empty(self):
        return self._size == 0

    def first(self):
        if self.is_empty():
            raise Exception("queue is empty")
        head= self._tail._next
        return head._val

    def enqueue(self , n):
        node = self._Node(n, None)
        # to make it circular
        #1 if empty create node and make it point to itself
        if self.is_empty():
            node._next = node
        # 2 else create node and make it point to head
        else:
            node._next = self._tail._next # head
            self._tail._next = node
        self._tail =node
        self ._size +=1

    def dequeue(self):
        if self.is_empty():
            raise Exception("empty Queue")
        head=self._tail._next
        if self._size ==1:
            self._tail=None
        else:
            self._tail._next = head._next
        self._size -=1

        return head._val

    def rotate(self):
        if self._size >0:
            self._tail = self._tail._next

if __name__ == '__main__':
    cq = CircularQueue()
    cq.enqueue(1)
    cq.enqueue(2)
    cq.enqueue(3)
    cq.enqueue(4)
    cq.enqueue(5)
    cq.rotate()
    print(cq.first())
    # 2
    cq.rotate()
    print(cq.first())
    # 3
    print(cq.dequeue())
    print(cq.dequeue())
    print(cq.dequeue())
    print(cq.dequeue())


