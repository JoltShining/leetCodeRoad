#!/usr/bin/env python37
# _*_ coding:utf-8 _*_
"""
Author : 'Shining'
Date:20-03-11
Describe:返回滑动窗口的最大值
"""


class Solution:

    def __init__(self,nums,k):

        self.nums = nums
        self.k = k

    def maxSlidingWindow1(self):
        """
        window 中存取的是索引
        :return:
        """

        if not self.nums:return []
        window, res = [], []
        for i, x in enumerate(self.nums):
            if i >= self.k and window[0] <= i-self.k:
                window.pop(0)
            while window and self.nums[window[-1]] <= x:
                window.pop()
            window.append(i)
            if i >= self.k - 1:
                res.append(self.nums[window[0]])
        return res

    def maxSlidingWindow2(self):
        """
        执行用时 :588 ms, 在所有 Python3 提交中击败了26.71%的用户
        内存消耗 :17.2 MB, 在所有 Python3 提交中击败了100.00%的用户
        :return:
        """

        res = []
        if not self.nums:return res
        if len(self.nums) <= self.k:
            res.append(max(self.nums))
        else:
            for i in range(len(self.nums)-self.k+1):
                res.append(max(self.nums[i:i+self.k]))
        return res


if __name__  == "__main__":

    temp = [1]
    k = 3

    solution = Solution(temp,k)
    print(solution.maxSlidingWindow2())
