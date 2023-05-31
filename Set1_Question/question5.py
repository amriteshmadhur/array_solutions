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


if __name__ == "__main__":
    #unittest.main(verbosity=2)
    #print("Nice job, 2/2 tests passed!")
    # Test the function
    nums1 = [1, 2, 3, 0, 0, 0]
    m = 3
    nums2 = [2, 5, 6]
    n = 3
    
    merged = merge(nums1, m, nums2, n)
    print(merged)
