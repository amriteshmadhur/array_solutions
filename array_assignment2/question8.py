# -*- coding: utf-8 -*-
"""

@author: amritesh
You are given an integer array nums and an integer k.

In one operation, you can choose any index i where 0 <= i < nums.length and change nums[i] to nums[i] + x where x is an integer from the range [-k, k]. You can apply this operation at most once for each index i.

The score of nums is the difference between the maximum and minimum elements in nums.

Return the minimum score of nums after applying the mentioned operation at most once for each index in it.

Example 1:
Input: nums = [1], k = 0
Output: 0

"""
def minimumScore(nums, k):
    min_val = float('inf')
    max_val = float('-inf')

    for num in nums:
        min_val = min(min_val, num)
        max_val = max(max_val, num)

    score = max_val - min_val
    return score

# Test the example
nums = [1]
k = 0
print(minimumScore(nums, k))



