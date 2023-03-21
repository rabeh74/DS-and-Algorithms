"""
Your input is an array of integers,
and you have to reorder its entries so that the even entries appear first
"""
# O(n) time and O(1) space
def even_odd(A):
    l,r=0,len(A)-1
    while l<r:
        if A[l] %2==0:
            l+=1

        else:
            # swap
            A[l], A[r]=A[r],A[l]
            r-=1
    return A

if __name__ == "__main__":
    A=[1,2,3,4,5,6,7,8,9,10]
    print(even_odd(A))
    #[10, 2, 8, 4, 6, 5, 7, 3, 9, 1]

    A=[3,2,4,1,7,4,3,9,22,3,5]
    print(even_odd(A))
    #[22, 2, 4, 4, 3, 3, 3, 9, 5, 7, 1]