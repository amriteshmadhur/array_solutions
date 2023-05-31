
"""
Created on Wed May 30 21:37:56 2023

@author: Amritesh

Q7: Given an integer array nums, move all 0's to the end of it while maintaining the relative order of the nonzero elements.
Note that you must do this in-place without making a copy of the array.
Example 1:
Input: nums = [0,1,0,3,12]
Output: [1,3,12,0,0]
"""
def push_zero_end(nums):
    slow = 0
    for fast in range(len(nums)):
        if nums[fast] != 0:
            nums[slow], nums[fast] = nums[fast], nums[slow]
            slow += 1

    for i in range(slow, len(nums)):
        nums[i] = 0



if __name__ == "__main__":
    #unittest.main(verbosity=2)
    #print("Nice job, 2/2 tests passed!")
    # Test the function
     # Test the function
     nums = [0, 1, 0, 3, 12]
     push_zero_end(nums)
     print(nums)

