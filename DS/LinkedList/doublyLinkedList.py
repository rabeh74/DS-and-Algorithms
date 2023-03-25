"""
private double linked list class , to prevent the user from accessing the
nodes directly(only the methods of the class can access the nodes)
"""
"""
using sentinel nodes to avoid special cases in insertions and deletions
"""
class _DoubleLinkedList:
    class _Node:
        __slots__ = "_next","_prev","_val"
        def __init__( self , val , next , prev):
            self._val=val
            self._next=next
            self._prev=prev

    def __init__(self):
        self._size=0
        self._head=self._Node(0, None, None)
        self._tail=self._Node(0, None, None)
        self._head._next , self._tail._prev = self._tail , self._head

    def _is_empty(self):
        return self._size ==0
    def __len__(self):
        return self._size

    def _insert_between(self , node1 , node2 , val):
        new_node=self._Node(val, node2, node1)
        node1._next=new_node
        node2._prev=new_node
        self._size +=1
        return new_node

    def _delete_node(self , node):
        prev=node._prev
        nex=node._next

        prev._next , nex._prev= nex , prev
        self._size -=1

        node._prev=node._next=None
        return node._val

class LinkedDequeue(_DoubleLinkedList):
    def first(self):
        if self._is_empty():
            raise Exception("empty deque")
        return self._head._next._val

    def last(self):
        if self._is_empty():
            raise Exception("empty deque")
        return self._tail._prev._val

    def insert_first(self , val):
        self._insert_between(self._head, self._head._next, val)

    def insert_last(self , val):
        self._insert_between(self._tail._prev, self._tail, val)

    def delete_first(self):
        if self._is_empty():
            raise Exception("empty deque")
        self._delete_node(self._head._next)

    def delete_last(self):
        if self._is_empty():
            raise Exception("empty deque")
        self._delete_node(self._tail._prev)

if __name__ == "__main__":
    deque=LinkedDequeue()
    deque.insert_first(1)
    deque.insert_first(2)
    deque.insert_last(3)
    deque.insert_last(4)
    print(deque.first())
    print(deque.last())
    deque.delete_first()
    deque.delete_last()
    print(deque.first())
    print(deque.last())