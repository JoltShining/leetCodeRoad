#!/usr/bin/env python37
# _*_ coding:utf-8 _*_
"""
Author : 'Shining'
Date:20-03-12
Describe:翻转矩阵
"""

class Solution:

    def transpose(self,nums):
        """
        执行用时 :80 ms, 在所有 Python3 提交中击败了81.53%的用户
        内存消耗 :14.1 MB, 在所有 Python3 提交中击败了12.32%的用户
        :param nums:
        :return:
        """
        if not nums:return []
        lengthItem = len(nums[0])
        res = []
        for i in range(lengthItem):
            temp = []
            for item in nums:
                temp.append(item[i])
            res.append(temp)
        return res


if __name__ == "__main__":

    solution = Solution()
    test = [[1,2,3],[4,5,6],[7,8,9]]
    print(solution.transpose(test))