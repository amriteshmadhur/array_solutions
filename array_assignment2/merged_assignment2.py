# -*- coding: utf-8 -*-
"""

@author: amritesh

Given an integer array nums of 2n integers, group these integers into n pairs (a1, b1), (a2, b2),..., (an, bn) such that the sum of min(ai, bi) for all i is maximized. Return the maximized sum.

Example 1:
Input: nums = [1,4,3,2]
Output: 4
"""
def arrayPairSum(nums):
    nums.sort()
    max_sum = 0
    for i in range(0, len(nums), 2):
        max_sum += nums[i]
    return max_sum


nums = [1, 4, 3, 2]
print(arrayPairSum(nums))



# -*- coding: utf-8 -*-
"""

@author: amritesh

Alice has n candies, where the ith candy is of type candyType[i]. Alice noticed that she started to gain weight, so she visited a doctor. 

The doctor advised Alice to only eat n / 2 of the candies she has (n is always even). Alice likes her candies very much, and she wants to eat the maximum number of different types of candies while still following the doctor's advice. 

Given the integer array candyType of length n, return the maximum number of different types of candies she can eat if she only eats n / 2 of them.

Example 1:
Input: candyType = [1,1,2,2,3,3]
Output: 3

Explanation: Alice can only eat 6 / 2 = 3 candies. Since there are only 3 types, she can eat one of each type.

"""

def distribute_candies(candyType):
    max_candies = len(candyType) // 2
    unique_candies = len(set(candyType))
    return min(unique_candies, max_candies)

candyType = [1, 1, 2, 2, 3, 3]
print(distribute_candies(candyType))  # Output: 3




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
# -*- coding: utf-8 -*-
"""

@author: amritesh

You have a long flowerbed in which some of the plots are planted, and some are not.
However, flowers cannot be planted in adjacent plots.
Given an integer array flowerbed containing 0's and 1's, where 0 means empty and 1 means not empty, and an integer n, return true if n new flowers can be planted in the flowerbed without violating the no-adjacent-flowers rule and false otherwise.

Example 1:
Input: flowerbed = [1,0,0,0,1], n = 1
Output: true
"""



def is_place_flower(flowerbed, n):
    count = 0
    length = len(flowerbed)
    i = 0

    while i < length:
        if flowerbed[i] == 0:
            if i == 0 or flowerbed[i - 1] == 0:
                if i == length - 1 or flowerbed[i + 1] == 0:
                    flowerbed[i] = 1
                    count += 1
                    i += 1

        if count >= n:
            return True

        i += 1

    return False

# Test case 1
flowerbed1 = [1, 0, 0, 0, 1]
n1 = 1
# One new flower can be planted in position 2.
# Result: True
expected1 = True

# Test case 2
flowerbed2 = [1, 0, 0, 0, 1]
n2 = 2
# Two new flowers cannot be planted without violating the rule of no adjacent flowers.
# Result: False
expected2 = False

# Test case 3
flowerbed3 = [0, 0, 0, 0, 0]
n3 = 3
# Three new flowers can be planted in any of the available plots.
# Result: True
expected3 = True

# Test case 4
flowerbed4 = [1, 0, 1, 0, 1]
n4 = 1
# One new flower cannot be planted without violating the rule of no adjacent flowers.
# Result: False
expected4 = False

# Test case 5
flowerbed5 = [0, 0, 0, 0, 0]
n5 = 0
# No new flowers need to be planted.
# Result: True
expected5 = True

# Run the tests
assert is_place_flower(flowerbed1, n1) == expected1
assert is_place_flower(flowerbed2, n2) == expected2
assert is_place_flower(flowerbed3, n3) == expected3
assert is_place_flower(flowerbed4, n4) == expected4
assert is_place_flower(flowerbed5, n5) == expected5

print("All test cases passed!")
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



# -*- coding: utf-8 -*-
"""

@author: amritesh

Given an array of integers nums which is sorted in ascending order, and an integer target,
write a function to search target in nums. If target exists, then return its index. Otherwise,
return -1.

You must write an algorithm with O(log n) runtime complexity.

Input: nums = [-1,0,3,5,9,12], target = 9
Output: 4

Explanation: 9 exists in nums and its index is 4
"""


def search(nums, target):
    left = 0
    right = len(nums) - 1

    while left <= right:
        mid = left + (right - left) // 2

        if nums[mid] == target:
            return mid
        elif nums[mid] < target:
            left = mid + 1
        else:
            right = mid - 1

    return -1


nums = [-1, 0, 3, 5, 9, 12]
target = 9
print(search(nums, target))

# -*- coding: utf-8 -*-
"""

@author: amritesh

"""



def is_mono(nums):
    n = len(nums)
    increasing = decreasing = True

    for i in range(1, n):
        if nums[i] < nums[i - 1]:
            increasing = False
        if nums[i] > nums[i - 1]:
            decreasing = False

    return increasing or decreasing

nums = [1, 2, 2, 3]
print(is_mono(nums))
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
def minm_score(nums, k):
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
print(minm_score(nums, k))



