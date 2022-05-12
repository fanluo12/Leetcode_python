# -*- coding: utf-8 -*-
"""
Created on Sun Feb 27 20:03:50 2022

@author: Fan Luo
"""
"""
637. Average of Levels in Binary Tree

Given the root of a binary tree, return the average value of the nodes on each level in the form of an array. 
Answers within 10-5 of the actual answer will be accepted.

Input: root = [3,9,20,null,null,15,7]
Output: [3.00000,14.50000,11.00000]
Explanation: The average value of nodes on level 0 is 3, on level 1 is 14.5, and on level 2 is 11.
Hence return [3, 14.5, 11].
"""
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def averageOfLevels(self, root):
        stack = [root]
        res = []
        while stack:
            length = len(stack)
            row = 0
            for i in range(length):
                node = stack.pop(0)
                row += node.val
                if node.left:
                    stack.append(node.left)
                if node.right:
                    stack.append(node.right)
            res.append(row / length)
        return res