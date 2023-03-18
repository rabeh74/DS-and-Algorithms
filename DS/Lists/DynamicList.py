import ctypes

class DynamicList:
    def __init__(self):
        self._n = 0
        self._capacity = 1
        self._A = self._make_array(self._capacity)

    def __len__(self):
        return self._n

    def __getitem__(self , idx):
        if idx < 0 or idx >= self._n:
            raise IndexError("Invalid index")
        return self._A[idx]

    def is_empty(self):
        return self._n ==0

    def append(self , num):
        if self._n == self._capacity:
            self._resize(2*self._capacity)
        self._A[self._n]=num
        self._n+=1

    def _resize(self , c):
        B= self._make_array(c)
        for i in range(self._n):
            B[i]=self._A[i]
        self._A=B
        self._capacity=c

    def _make_array(self , c):
        return (c*ctypes.py_object)()

    def insert(self , idx , num):
        if not 0<=idx < self._n:
            raise IndexError("Invalid index")
        if self._n==self._capacity:
            self._resize(2*self._capacity)
        # shift elements to the right
        for i in range(self._n , idx , -1):
            self._A[i]=self._A[i-1]

        self._A[idx]=num
        self._n +=1

    def pop(self):
        if self.is_empty():
            raise IndexError("List is empty")
        self._n-=1
        return self._A[self._n]

    def remove(self , idx):
        if not 0<=idx < self._n:
            raise IndexError("Invalid index")
        # meve elements to the left
        for i in range(idx , self._n-1):
            self._A[i]=self._A[i+1]

        self._n -=1
        if self._n < self._capacity//4:
            self._resize(self._capacity//2)
    # delete the first occurence of num
    def delete(self,num):
        for i in range(self._n):
            v=self._A[i]
            if v == num:
                self.remove(i)
                return True
        return False

    def find(self , num):
        for i in range(self._n):
            v=self._A[i]
            if v == num:
                return i
        return -1
    def __str__(self):
        return str(self._A[:self._n])

if __name__ == "__main__":
    # test
    L = DynamicList()
    for i in range(10):
        L.append(i)
    print(L)
    L.insert(5, 10)
    print(L)
    L.remove(5)
    print(L)
    L.pop()
    print(L)
    L.delete(5)
    print(L)
    print(L.find(5))
    print(L.find(6))
    print(L[7])


