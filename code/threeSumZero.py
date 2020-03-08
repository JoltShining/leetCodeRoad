#!/usr/bin/env python37
# _*_ coding:utf-8 _*_
"""
Author : 'Shining'
Date:2020-03-08
Describe:三个数之和为0,返回不重复的组合
"""
class Solution:

    def threeSumHard(self,nums):
        """
        时间不通过
        :param nums:
        :return:
        """
        length = len(nums)
        res = []
        for i in range(length-2):
            for j in range(i+1,length-1):
                for k in range(j+1,length):
                    if nums[i] + nums[j] + nums[k] == 0:
                        temp = [nums[i], nums[j], nums[k]]
                        temp.sort()
                        if temp not in res:
                            res.append(temp)

        return res


    def threeSumoptA(self,nums):
        """
        时间不通过
        :param nums:
        :return:
        """

        length = len(nums)
        res = []
        hash_map = dict()
        for i,x in enumerate(nums):
            for j in range(i+1,length):
                if -(x+nums[j]) in hash_map and hash_map[-(x+nums[j])] not in (i,j):
                    temp = [x,nums[j],-(x+nums[j])]
                    temp.sort()
                    if temp not in res:
                        res.append(temp)
            hash_map[x] = i
        return res

    def threeSum(self, nums):
        """
        超出时间限制,不符合要求
        :param nums:
        :return:
        """
        res = []
        length = len(nums)
        for i in range(length - 1):
            for j in range(i+1, length):
                target = -(nums[i] + nums[j])
                if target in nums and nums.index(target) not in(i,j):
                    temp = [nums[i],nums[j],-(nums[i]+nums[j])]
                    temp.sort()
                    if temp not in res:
                        res.append(temp)
        return res

    def threeSumOptB(self,nums):
        '''
        pass
        :param nums:
        :return:
        '''

        length = len(nums)
        nums.sort()
        i = 0
        res = []
        for i in range(length):
            if i > 0 and nums[i] == nums[i-1]:
                continue
            else:
                target = -nums[i]
                j = i+1
                k = length - 1
                while j < k:
                    if nums[j] + nums[k] == target:
                        temp = [nums[i],nums[j],nums[k]]
                        res.append(temp)
                        j += 1
                        k -= 1
                        while(j < length and nums[j] == nums[j-1]):
                            j += 1
                        while(k > j and nums[k] == nums[k+1]):
                            k -= 1
                    elif(nums[j]+nums[k]) > target:
                        k -= 1
                    else:
                        j +=1
        return res





if __name__ == "__main__":

    temp = [-1,0,1,2,-1,-4]

    solution = Solution()
    print(solution.threeSum(temp))
    print(solution.threeSumHard(temp))
    print(solution.threeSumoptA(temp))
    print(solution.threeSumOptB(temp))