# -*- coding: utf-8 -*-
"""
Created on Mon Apr 11 19:51:04 2022

@author: Fan Luo
"""
"""
1921. Eliminate Maximum Number of Monsters

You are playing a video game where you are defending your city from a group of n monsters. You are given a 0-indexed integer array dist of size n, where dist[i] is the initial distance in kilometers of the ith monster from the city.

The monsters walk toward the city at a constant speed. The speed of each monster is given to you in an integer array speed of size n, where speed[i] is the speed of the ith monster in kilometers per minute.

You have a weapon that, once fully charged, can eliminate a single monster. However, the weapon takes one minute to charge.The weapon is fully charged at the very start.

You lose when any monster reaches your city. If a monster reaches the city at the exact moment the weapon is fully charged, it counts as a loss, and the game ends before you can use your weapon.

Return the maximum number of monsters that you can eliminate before you lose, or n if you can eliminate all the monsters before they reach the city.

Input: dist = [1,3,4], speed = [1,1,1]
Output: 3
Explanation:
In the beginning, the distances of the monsters are [1,3,4]. You eliminate the first monster.
After a minute, the distances of the monsters are [X,2,3]. You eliminate the second monster.
After a minute, the distances of the monsters are [X,X,2]. You eliminate the thrid monster.
All 3 monsters can be eliminated.
"""
import math

class Solution:
    def eliminateMaximum(self, dist, speed):
        minReach = []
        for d, s in zip(dist, speed):
            minute = math.ceil(d / s)
            minReach.append(minute)
            
        minReach.sort()
        res = 0
        for i in range(len(minReach)):
            if i >= minReach[i]:
                return res
            res += 1
            
        return res