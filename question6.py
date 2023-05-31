# -*- coding: utf-8 -*-
"""
Created on Wed May 30 21:37:56 2023

@author: Amritesh
Given an integer array nums, return true if any value appears at least twice in the array, and return false if every element is distinct.
**Example 1:**
Input: nums = [1,2,3,1]

Output: true

"""

def find_duplicate(nums):
    unique_set = set()
    for num in nums:
        if num in unique_set:
            return True
        unique_set.add(num)
    return False

if __name__ == "__main__":
    # Test the function
    nums = [1, 2, 3, 1]
    result = find_duplicate(nums)
    print(result)