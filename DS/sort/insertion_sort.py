# take O(n2) time
def insertion_sort(A):
    n=len(A)
    for i in range(1,n):
        cur_val=A[i]
        j=i
        # find correct pos in sorted arr A[:J]
        while j >0 and A[j-1] > cur_val:
            #shift right
            A[j]=A[j-1]
            j-=1
        A[j]=cur_val
    return A

