# -*- coding: utf-8 -*-
"""

@author: amritesh
Given an integer array nums, find three numbers whose product is maximum and return the maximum product.

Example 1:
Input: nums = [1,2,3]
Output: 6
"""

def max_product(nums):
    nums.sort()
    product1 = nums[-1] * nums[-2] * nums[-3]
    product2 = nums[0] * nums[1] * nums[-1]
    return max(product1, product2)

nums = [1, 2, 3]
print(max_product(nums))



