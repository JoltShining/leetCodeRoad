#!/usr/bin/env python37
# _*_ coding:utf-8 _*_
"""
Author : 'Shining'
Date:2019-12-14
Describe:algo example
"""


# insert sort by rec
def ins_sort_rec(seq,i):
    if i == 0: return
    ins_sort_rec(seq, i - 1)
    j = i
    while j > 0 and seq[j-1] > seq[j]:
        seq[j-1], seq[j] = seq[j], seq[j-1]
        j -= 1

def ins_sort(seq):
    for i in range(len(seq)):
        j = i
        while j > 0 and seq[j-1] > seq[j]:
            seq[j-1], seq[j] = seq[j], seq[j-1]
            j -= 1


def sel_sort_rec(seq, i):
    if i == 0: return
    max_j = i
    for j in range(i):
        if seq[j] > seq[max_j]: max_j = j
    seq[i], seq[max_j] = seq[max_j], seq[i]
    sel_sort_rec(seq, i-1)


def sel_sort(seq):
    for i in range(len(seq)-1,0,-1):
        max_j = i
        for j in range(i):
            if seq[j] > seq[max_j]: max_j = j
        seq[i], seq[max_j] = seq[max_j],seq[i]


if __name__ == "__main__":
    seq = [1,3,9,4,6,7,2,1,8]
    print("seq is {}".format(seq))
    print("递归插入排序调用结果:{},sep:{}".format(ins_sort_rec(seq,8),seq))
    seq = [1, 3, 9, 4, 6, 7, 2, 1, 11]
    print("插入排序调用结果:{},seq:{}".format(ins_sort(seq),seq))
    seq = [1, 5, 9, 4, 6, 7, 2, 1, 8]
    print("递归选择调用排序结果:{},seq:{}".format(sel_sort_rec(seq,8),seq))
    seq = [1, 3, 9, 4, 6, 7, 2, 1, 8]
    print("选择排序的结果是:{},seq:{}".format(sel_sort(seq),seq))



