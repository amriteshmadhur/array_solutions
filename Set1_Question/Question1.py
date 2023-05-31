# -*- coding: utf-8 -*-
"""
Created on Wed May 27th 20:13:33 2023

@author: Amritesh

Given an array of integers nums and an integer target, return indices of the 
two numbers such that they add up to target.You may assume that each input
would have exactly one solution, and you may not use the same element twice.

You can return the answer in any order.
Example:
Input: nums = [2,7,11,15], target = 9
Output0 [0,1]

"""
def get_indices(nums, target):
    left = 0
    right = len(nums) - 1

    while left < right:
        sum = nums[left] + nums[right]
        if sum == target:
            return [left, right]
        elif sum < target:
            left += 1
        else:
            right -= 1

    return []  # No solution found

if __name__ == "__main__":
    # Test the function
    nums = [2, 7, 11, 15]
    target = 9
    result = get_indices(nums, target)
    print(result)


