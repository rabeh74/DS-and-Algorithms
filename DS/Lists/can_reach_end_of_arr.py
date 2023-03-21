""" Write a program which takes an array of n integers,
 where A[i] denotes the maximum you can advance from index l,
 and retums whether it is possible to advance
 to the last index starting from the beginning of the array."""

def canJump(nums):
    furthest_reach_so_far,last_idx = 0,len(nums)-1
    i=0
    while i <= furthest_reach_so_far and furthest_reach_so_far <last_idx:
        furthest_reach_so_far = max(furthest_reach_so_far, i+nums[i])
        i+=1
    return furthest_reach_so_far >= last_idx


def canJump2(nums):
    n=len(nums)
    needed_idx=1
    for i in reversed(range(n-1)):
        if needed_idx <=nums[i]:
            needed_idx=1
        else:
            needed_idx +=1
    return needed_idx ==1

if __name__ == "__main__":
    print(canJump([3,3,1,0,2,0,1]))
    print(canJump2([3,3,1,0,2,0,1]))
    # true
    print(canJump([3,2,0,0,2,0,1]))
    print(canJump2([3,2,0,0,2,0,1]))
    # false


