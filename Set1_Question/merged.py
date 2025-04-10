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
    print(result)# -*- coding: utf-8 -*-
"""
Created on Wed May 30 21:37:56 2023

@author: Amritesh
Q3. You are given a large integer represented as an integer array digits, where each digits[i] is the ith digit of the integer. The digits are ordered from most significant to least significant in left-to-right order. The large integer does not contain any leading 0's.
Increment the large integer by one and return the resulting array of digits.
Example 1:
Input: digits = [1,2,3]
Output: [1,2,4]
The array represents the integer 123.
incrementing by one gives 123 + 1 = 124.
Thus, the result should be [1,2,4].

"""

def add_one(digits):
    carry = 1
    n = len(digits)

    for i in range(n - 1, -1, -1):
        digits[i] += carry
        carry = digits[i] // 10
        digits[i] %= 10

    if carry:
        digits.insert(0, 1)

    return digits


# -*- coding: utf-8 -*-
"""
Created on Wed May 30 21:37:56 2023

@author: Amritesh

Q5: You are given two integer arrays nums1 and nums2, sorted in non-decreasing order, and two integers m and n, representing the number of elements in nums1 and nums2 respectively.
Merge nums1 and nums2 into a single array sorted in non-decreasing order.
The final sorted array should not be returned by the function, but instead be stored inside the array nums1. To accommodate this, nums1 has a length of m + n, where the first m elements denote the elements that should be merged, and the last n elements are set to 0 and should be ignored. nums2 has a length of n.
Example 1:
Input: nums1 = [1,2,3,0,0,0], m = 3, nums2 = [2,5,6], n = 3
Output: [1,2,2,3,5,6]
Explanation: The arrays we are merging are [1,2,3] and [2,5,6].
The result of the merge is [1,2,2,3,5,6] with the underlined elements coming from nums1.
"""
def merge(nums1, m, nums2, n):
    i = m - 1
    j = n - 1
    k = m + n - 1

    while i >= 0 and j >= 0:
        if nums1[i] >= nums2[j]:
            nums1[k] = nums1[i]
            i -= 1
        else:
            nums1[k] = nums2[j]
            j -= 1
        k -= 1

    # If there are remaining elements in nums2, copy them to nums1
    while j >= 0:
        nums1[k] = nums2[j]
        j -= 1
        k -= 1

    return nums1


import unittest

class Test(unittest.TestCase):
    def test_1(self):
        assert merge([1,2,3], 3, [2,5,6], 3) == [1,2,2,3,5,6]
        print(
            "PASSED: merge([1,2,3], 3, [2,5,6], 3) should return '[1,2,2,3,5,6]'"
        )

    def test_2(self):
        assert merge([1,10,55,66], 4, [21,48,68,80], 4) == [1,10,21,48,55,66,68,80]
        print("PASSED: merge([1,10,55,66], 4, [21,48,68,80], 4) should return '[1,10,21,48,55,66,68,80]'")


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




# -*- coding: utf-8 -*-
"""
Created on Wed May 31 22:29:02 2023

@author: Amritesh
Q. You have a set of integers s, which originally contains all the numbers from 1 to n. Unfortunately, due to some error, one of the numbers in s got duplicated to another number in the set, which results in repetition of one number and loss of another number
You are given an integer array nums representing the data status of this set after the error.
Find the number that occurs twice and the number that is missing and return them in the form of an array.
"""

def find_missing_num(nums):
    numSet = set()
    duplicate = -1
    n = len(nums)

    for num in nums:
        if num not in numSet:
            numSet.add(num)
        else:
            duplicate = num

    missing = set(range(1, n+1)) - numSet

    return [duplicate, missing.pop()]


if __name__ == "__main__":
    # Test the function
    nums = [2, 7, 11, 15]
    target = 9
    result = get_indices(nums, target)
    print(result)

    # Test the function
    nums = [1, 2, 2, 4]
    result = find_missing_num(nums)
    print(result)
    


    # Test the function
    nums = [0, 1, 2, 2, 3, 0, 4, 2]
    val = 2
    k = remove_elements(nums, val)
    print( k, ",", "nums = ", nums)

    #unittest.main(verbosity=2)
    #print("Nice job, 2/2 tests passed!")
    # Test the function
     # Test the function
    nums = [0, 1, 0, 3, 12]
    push_zero_end(nums)
    print(nums)

    # Test the function
    nums = [1, 2, 3, 1]
    result = find_duplicate(nums)
    print(result)



    #unittest.main(verbosity=2)
    #print("Nice job, 2/2 tests passed!")
    # Test the function
    nums1 = [1, 2, 3, 0, 0, 0]
    m = 3
    nums2 = [2, 5, 6]
    n = 3
    
    merged = merge(nums1, m, nums2, n)
    print(merged)


    # Test the function
    digits = [1, 2, 3]
    result = add_one(digits)
    print(result)