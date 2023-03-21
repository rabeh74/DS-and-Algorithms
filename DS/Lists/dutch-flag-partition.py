"""Write a program that takes an array A and an index i rnto A,
 and rearranges the elements such that all elements less than A[r] (the "pivot") appear first
, followed by elements equal to the pivot,
 followed by elements greater than the pivot."""

def dutch_flag_partition(pivot_index, A):
    smaller,equal ,larger = 0,0,len(A)-1
    pivot=A[pivot_index]

    while equal <= larger:
        # make from 0 to samller less than pivot
        if A[equal] < pivot:
            A[equal],A[smaller]=A[smaller] , A[equal]
            smaller +=1
            equal +=1
        # make from smaller to equal = pivot
        elif A[equal]==pivot:
            equal +=1
            # make from larger to length greater
        else:
            A[equal],A[larger]=A[larger] , A[equal]
            larger -=1
    return A



if __name__ == "__main__":
    A=[3,2,7,5,3,0,8,7,3,6,2]
    pivot_index=4
    print(dutch_flag_partition(pivot_index,A))

