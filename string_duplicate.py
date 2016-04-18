#!/usr/bin/env python
# -*- coding: utf-8 -*-

__author__ = 'lina'
__date__ = '16/4/18'


def get_first_single(string):

    # 获取字符串中第一个只出现一次的字符的index

    if not string:
        return -1
    length = len(string)
    char_count = dict()
    for index in range(0, length):
        char = string[index]
        # if string.count(char) == 1:
        #     return index
        if char in char_count.keys():
            char_count[char] += 1

        else:
            char_count[char] = 1
        index += 1

    for index in range(0, length):
        char = string[index]
        if char_count[char] == 1:
            return index

        index += 1

    return -1

if __name__ == "__main__":


    a = "bdldjfsewhnasbl"

    print get_first_single(a)