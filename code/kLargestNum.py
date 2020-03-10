#!/usr/bin/env python37
# _*_ coding:utf-8 _*_
"""
Author : 'Shining'
Date:20-03-10
Describe:
## 实时判断数据流第k大的元素
* 保存前k个 最大值
 - k.Max ==> sorted
 - 复杂度 N\*K\*LogK
* 维护一个最小堆(min Heap)
 - size = k
 - 复杂度 N\*logK
"""
import heapq

class Solution:

    def __init__(self,k, nums):
        self.pool = nums
        heapq.heapify(self.pool)
        self.k = k
        self.nums = nums
        self.nums.sort(reverse = True)
        while len(self.pool) > k:
            heapq.heappop(self.pool)
        while len(self.nums)>k:
            self.nums.pop()


    def add(self,val):
        self.nums.append(val)
        self.nums.sort(reverse=True)
        if (len(self.nums)) > self.k:
            self.nums.pop()
        elif (len(self.nums)) <self.k:
            return None
        return self.nums[-1]

    def flat(self,lista):
        res = []
        for i in lista:
            if isinstance(i,list):
                res.extend(self.flat(i))
            else:
                res.append(i)
        return res

    def kLargestnumOptA(self,val):
        if len(self.pool) < self.k:
            heapq.heappush(self.pool,val)
        elif val > self.pool[0]:
            heapq.heapreplace(self.pool,val)
        return self.pool[0]

if __name__ == "__main__":


    temp = [4]
    solution = Solution(3, temp)
    print(solution.add(3))
    print(solution.add(5))
    print(solution.add(10))
    print(solution.add(9))
    print(solution.add(4))