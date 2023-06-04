# -*- coding: utf-8 -*-
"""

@author: amritesh

We define a harmonious array as an array where the difference between its maximum value
and its minimum value is exactly 1.

Given an integer array nums, return the length of its longest harmonious subsequence
among all its possible subsequences.

A subsequence of an array is a sequence that can be derived from the array by deleting some or no elements without changing the order of the remaining elements.

Example 1:
Input: nums = [1,3,2,2,5,2,3,7]
Output: 5

Explanation: The longest harmonious subsequence is [3,2,2,2,3].
"""


def find_lhs(nums):
    count = {}
    longest = 0
    
    # Count the frequency of each number in the array
    for num in nums:
        count[num] = count.get(num, 0) + 1
    
    # Check each number in the count dictionary
    for num in count:
        # If the current number and the next consecutive number are both present in the count dictionary,
        # calculate the length of the harmonious subsequence
        if num + 1 in count:
            length = count[num] + count[num + 1]
            longest = max(longest, length)
    
    return longest

# Example test case
nums = [1, 3, 2, 2, 5, 2, 3, 7]
print(find_lhs(nums))  # Output: 5

# Additional test cases
nums = [1, 1, 1, 1]
print(find_lhs(nums))  # Output: 0 (No harmonious subsequence)

nums = [1, 2, 3, 4, 5]
print(find_lhs(nums))  # Output: 2 (Longest harmonious subsequence: [1, 2])

nums = [1, 2, 2, 3, 4, 4, 5, 5, 5]
print(find_lhs(nums))  # Output: 5 (Longest harmonious subsequence: [2, 2, 3, 4, 4])
