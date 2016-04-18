#!/usr/bin/env python
# -*- coding: utf-8 -*-

__author__ = 'lina'
__date__ = '16/4/17'


def ajust_array(array, left, right):

    i = left
    j = right
    x = array[left]

    while i < j:
        while i < j and array[j] > x:
            j -= 1

        if array[j] < x:
            array[i] = array[j]
            i += 1

        while i < j and array[i] < x:
            i += 1

        if array[i] > x:
            array[j] = array[i]
            j -= 1
    array[i] = x

    return i


def quick_sort(array, l, r):

    i = ajust_array(array, l, r)

    # prevent infinite loop
    if l < i:
        quick_sort(array, l, i-1)

    if i < r:
        quick_sort(array, i+1, r)

    return array


if __name__ == "__main__":
    a = [41, 27, 38, 43, 19, 67, 92, 45, 10, 31]

    length = len(a)
    r = len(a)-1

    print quick_sort(a, 0, r)




