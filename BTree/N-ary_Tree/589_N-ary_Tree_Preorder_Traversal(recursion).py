# -*- coding: utf-8 -*-
"""
Created on Sat Feb 12 13:31:53 2022

@author: Fan Luo
"""
"""
589. N-ary Tree Preorder Traversal

Given the root of an n-ary tree, return the preorder traversal of its nodes' values.

Nary-Tree input serialization is represented in their level order traversal. 
Each group of children is separated by the null value (See examples)

Input: root = [1,null,3,2,4,null,5,6]
Output: [1,3,5,6,2,4]
"""

class Node:
    def __init__(self, val=None, children=None):
        self.val = val
        self.children = children
        
        
class Solution:
    def preorder(self, root):
        res = []
        
        def dfs(root):
            if not root:
                return
            
            res.append(root.val)
            
            for child in root.children:
                dfs(child)
                
        dfs(root)
        return res