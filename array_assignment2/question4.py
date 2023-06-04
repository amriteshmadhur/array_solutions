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
