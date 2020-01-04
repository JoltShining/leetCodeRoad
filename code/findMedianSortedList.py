#!/usr/bin/env python37
# _*_ coding:utf-8 _*_
"""
Author : 'Shining'
Date:2020-01-04
Describe:algo example leetcode find two sort list median and O(log(m+n)),m,n is list length
"""

class FindMedianSortedList:

    def find_median_two_sorted_list(self,listA,listB):
        #  list A的长度小于等于 list B的长度
        if len(listA) > len(listB):
            listA, listB = listB, listA
        lengthA,lengthB = len(listA),len(listB)
        length = lengthA + lengthB
        medium = length // 2
        # listA 最大值小于listB的最小值，取值在A的最后一个元素或全部在B中
        if listA[lengthA - 1] <= listB[0]:
            if length % 2 == 0:
                if length / 2  == lengthA:
                    return (listA[lengthA-1] + listB[0]) / 2
                else:
                    return (listB[medium - lengthA -1] + listB[medium-lengthA]) / 2
            else:
                return listB[medium-lengthA]
        # list A最小值大于list B的最大值，中间值在B或A的第一个元素处取
        elif listA[0] >= listB[lengthB-1]:
            if length % 2 == 0:
                if length / 2 == length:
                    return (listB[lengthB-1] + listA[0]) / 2
                else:
                    return (listB[medium - 1] + listB[medium]) / 2
            else:
                return listB[medium]
        low = 0
        high = lengthA
        # 取list A 和list B的中间的值
        while low <= high:
            posA = (low + high) // 2
            posB = (lengthA + lengthB +1) // 2 - posA

            leftA = 0 if posA == 0 else listA[posA-1]
            leftB = 0 if posB == 0 else listB[posB-1]

            rightA = 0 if posA == 0 else listA[posA]
            rightB = 0 if posB == 0 else listB[posB]

            if leftA <= rightB and leftB <= rightA:
                if (lengthA + lengthB) % 2 == 0:
                    return (max(leftA,leftB) + min(rightA,rightB)) / 2
                else:
                    return max(leftA,leftB)
            elif rightA < leftB:
                low = posA + 1
            else:
                high = posA - 1


if __name__ == "__main__":

    listA = [1,3,8,9,15]
    listB = [17,18,18,19,21,25]
    listC = [28,30]
    listD = [4,4,8]
    listF = [1,3,29]
    listE = [4,9,10,25]
    findmedian = FindMedianSortedList()
    print(findmedian.find_median_two_sorted_list(listA,listB))
    print(findmedian.find_median_two_sorted_list(listC, listD))
    print(findmedian.find_median_two_sorted_list(listE, listF))
