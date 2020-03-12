#!/usr/bin/env python37
# _*_ coding:utf-8 _*_
"""
Author : 'Shining'
Date:20-03-11
Describe:三枚石子放置在数轴上，位置分别为 a，b，c。每一回合，我们假设这三枚石子当前分别位于位置 x, y, z 且 x < y < z。从位置 x 或者是位置 z 拿起一枚石子，并将该石子移动到某一整数位置 k 处，其中 x < k < z 且 k != y。
当你无法进行任何移动时，即，这些石子的位置连续时，游戏结束。要使游戏结束，你可以执行的最小和最大移动次数分别是多少？ 以长度为 2 的数组形式返回答案：answer = [minimum_moves, maximum_moves]
来源:力扣
"""

class Solution:

    def numMoveStone(self,nums):

        nums.sort()
        a,b,c = nums[0],nums[1],nums[2]
        max = c - b + a - 2
        min = 2
        if c - b == 1 and b-a == 1:
            min = 0
        elif b - a == 1 or c - b == 1:
            min = 1
        elif c - b == 2 or b - a == 2:
            min = 1
        return [min,max]

