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
    nums = [1, 2, 2, 4]
    result = find_missing_num(nums)
    print(result)
