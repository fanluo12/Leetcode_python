# -*- coding: utf-8 -*-
"""
Created on Sat Apr 30 14:38:56 2022

@author: Fan Luo
"""
"""
1095. Find in Mountain Array

(This problem is an interactive problem.)

You may recall that an array arr is a mountain array if and only if:

arr.length >= 3
There exists some i with 0 < i < arr.length - 1 such that:
arr[0] < arr[1] < ... < arr[i - 1] < arr[i]
arr[i] > arr[i + 1] > ... > arr[arr.length - 1]
Given a mountain array mountainArr, return the minimum index such that mountainArr.get(index) == target. If such an index does not exist, return -1.

You cannot access the mountain array directly. You may only access the array using a MountainArray interface:

MountainArray.get(k) returns the element of the array at index k (0-indexed).
MountainArray.length() returns the length of the array.
Submissions making more than 100 calls to MountainArray.get will be judged Wrong Answer. Also, any solutions that attempt to circumvent the judge will result in disqualification.

Input: array = [1,2,3,4,5,3,1], target = 3
Output: 2
Explanation: 3 exists in the array, at index=2 and index=5. Return the minimum index, which is 2.
"""
class MountainArray(object):
   def get(self, index):
       """
       :type index: int
       :rtype int
       """

   def length(self):
       """
       :rtype int
       """
       
class Solution:
    def findInMountainArray(self, target, mountain_arr):
        n = mountain_arr.length()
        l, r = 0, n - 1
        while l < r:
            m = (l + r) // 2
            if mountain_arr.get(m) < mountain_arr.get(m + 1):
                l = m + 1
            else:
                r = m
        peak = l
        if mountain_arr.get(peak) == target:
            return peak
        
        l, r = 0, peak - 1
        while l <= r:
            m = (l + r) // 2
            cur = mountain_arr.get(m)
            if cur == target:
                return m
            elif cur > target:
                r = m - 1
            else:
                l = m + 1
                
        l, r = peak + 1, n - 1
        while l <= r:
            m = (l + r) // 2
            cur = mountain_arr.get(m)
            if cur == target:
                return m
            elif cur > target:
                l = m + 1
            else:
                r = m - 1
        return -1