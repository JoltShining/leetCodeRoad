#!/usr/bin/env python37
# _*_ coding:utf-8 _*_
"""
Author : 'Shining'
Date:20-03-12
Describe:string 列表中所有字符串最长公共前缀
"""

class Solution:

    def longestCommonPrefix(self,strList):
        """
        暴力算法 时间和空间复杂度较差
        执行用时 :72 ms, 在所有 Python3 提交中击败了5.40%的用户
        内存消耗 :13.6 MB, 在所有 Python3 提交中击败了5.09%的用户
        :param strList:
        :return:
        """
        print('this')
        if not strList: return ''
        temp = sorted(strList,key=len)
        print(temp)
        minLength = len(temp[0])
        strLength = len(strList)
        res= ''
        i,j = 0,0
        while j < minLength:
            i = 0
            while i < strLength-1:
                if temp[i][j] == temp[i+1][j]:
                    i += 1
                    continue
                else:
                    return res
            res += temp[i][j]
            j += 1
        return res

    def longestCommonPrefixOptA(self,strs):
        """
        报错
        :param strs:
        :return:
        """
        if not strs:return ''
        res = ''
        prefix = strs[0]
        for i in range(1,len(strs)):
            while (strs[i].index(prefix) != 0):
                prefix = prefix[0:len(strs[0])-1]
            if not prefix:
                return ''
        return prefix

    def longestCommonPrefixOptB(self,strs):
        """
        zip() 函数用于将可迭代的对象作为参数，将对象中对应的元素打包成一个个元组，然后返回由这些元组组成的列表。
        如果各个迭代器的元素个数不一致，则返回列表长度与最短的对象相同，利用 * 号操作符，可以将元组解压为列表。
        :param strs:
        :return:
        """

        if not strs: return ""
        print(*strs)
        print(list(zip(*strs)))
        ss = list(map(set, zip(*strs)))
        print(ss)
        res = ""
        for i, x in enumerate(ss):
            x = list(x)
            if len(x) > 1:
                break
            res = res + x[0]
        return res

    def longestCommonPrefixOptC(self,strs):

        if not strs: return ""
        s1 = min(strs)
        s2 = max(strs)
        for i, x in enumerate(s1):
            if x != s2[i]:
                return s2[:i]
        return s1

if __name__ == "__main__":

    solution = Solution()
    test = ["flower","flow","flight"]
    test1 = ["aa","a"]
    print(solution.longestCommonPrefixOptB(test))