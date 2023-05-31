# -*- coding: utf-8 -*-
"""
Created on Wed May 30 21:37:56 2023

@author: Amritesh
Q3. Given a sorted array of distinct integers and a target value, return the index if the target is found. If not, return the index where it would be if it were inserted in order.
You must write an algorithm with O(log n) runtime complexity.
Example 1:
Input: nums = [1,3,5,6], target = 5
Output: 2

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