#!/usr/bin/env python37
# _*_ coding:utf-8 _*_
"""
Author : 'Shining'
Date:2020-01-07
Describe:find a longest substring of a string
"""


class LongestSubstring:

    def find_longest_substring(self, s):

        if s == '':
            return 0,1
        elif len(s) == 1:
            return 1,1

        maxLength = 0
        count = 0
        for i in range(len(s)-1):
            temp = set()
            temp.add(s[i])
            for j in range(i+1,len(s)):
                temp.add(s[j])
                if len(temp) == j-i+1:
                    count += 1
                    if maxLength < len(temp):
                        maxLength = len(temp)
                else:
                    count += 1
                    if maxLength < len(temp):
                        maxLength = len(temp)
                    continue

        return maxLength, count




if __name__ == "__main__":

    s1 = 'abc'
    s2 = 'aaaa'
    s3 = ''
    s4 = 'abcdabcbb'
    s5 = 'd'
    s6 = "abcdefghabcdefgabcdeabcdabc"
    strData = [s1,s2,s3,s4,s5,s6]
    findLongestSubstring = LongestSubstring()

    for data in strData:
        times,count = findLongestSubstring.find_longest_substring(data)
        print("{} 字符串的最大子字符串长度为:{},计算次数为{}.".format
              (data,times,count))