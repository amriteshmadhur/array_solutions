# -*- coding: utf-8 -*-
"""
Created on Wed May 31 20:24:52 2023 

@author: Amritesh
Given an integer array nums and an integer val, remove all occurrences of val in nums in-place. The order of the elements may be changed. Then return the number of elements in nums which are not equal to val.
Consider the number of elements in nums which are not equal to val be k, to get accepted, you need to do the following things:
Change the array nums such that the first k elements of nums contain the elements which are not equal to val. The remaining elements of nums are not important as well as the size of nums.
 Return k.

**Example :**
Input: nums = [3,2,2,3], val = 3
Output: 2, nums = [2,2,_*,_*]

"""

def remove_elements(nums, val):
    j = 0
    for i in range(len(nums)):
        if nums[i] != val:
            nums[j] = nums[i]
            j += 1
    for i in range(j, len(nums)):
        nums[i] = "_"
    
    return j


if __name__ == "__main__":

    # Test the function
    nums = [0, 1, 2, 2, 3, 0, 4, 2]
    val = 2
    k = remove_elements(nums, val)
    print( k, ",", "nums = ", nums)
    

     
