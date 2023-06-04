# -*- coding: utf-8 -*-
"""

@author: amritesh

"""



def isMonotonic(nums):
    n = len(nums)
    increasing = decreasing = True

    for i in range(1, n):
        if nums[i] < nums[i - 1]:
            increasing = False
        if nums[i] > nums[i - 1]:
            decreasing = False

    return increasing or decreasing

nums = [1, 2, 2, 3]
print(isMonotonic(nums))
