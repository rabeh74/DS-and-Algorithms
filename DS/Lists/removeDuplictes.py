"""

Write a program which takes as input a sorted array and updates it
 so that all duplicates have been removed and the remaining elements
  have been shifted left to fill the emptied indices
. Return the number of valid elements. Many languages have library functions
 for performing this operation- you cannot use these functions.
Hint:There is an O(n) time and O(1) space solution.

"""
def removeDuplicates(nums):
        if not nums:
            return 0
        valid_idx=1

        for i in range(1, len(nums)):
            if nums[i]!=nums[i-1]:
                nums[valid_idx]=nums[i]
                valid_idx +=1

        return valid_idx , nums[:valid_idx]

if __name__ == "__main__":
    nums=[2,3,5,5,7,11,11,11,13]
    print(removeDuplicates(nums))
    #6 , [2, 3, 5, 7, 11, 13]