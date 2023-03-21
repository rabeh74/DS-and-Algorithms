"""
Given a non-empty array of digits representing a non-negative integer,
 plus one to the integer."""
 
# O(n) time | O(1) space
def plusOne( digits):
        idx=len(digits)-1
        rem=0
        while idx >=0 :
            if digits[idx]==9:
                digits[idx]=0
            else:
                digits[idx] +=1
                break
            idx -=1
        if digits[0]==0:
            return [1]+digits
        return digits
if __name__ == "__main__":
    print(plusOne([1,2,3]))
    #[1, 2, 4]
    print(plusOne([1,2,9]))
    #[1, 3, 0]
    print(plusOne([9,9,9]))
    #[1, 0, 0, 0]
    print(plusOne([1,9,9]))
    #[2, 0, 0]
