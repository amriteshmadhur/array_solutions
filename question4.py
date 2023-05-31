# -*- coding: utf-8 -*-
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


if __name__ == "__main__":
    # Test the function
    digits = [1, 2, 3]
    result = add_one(digits)
    print(result)
