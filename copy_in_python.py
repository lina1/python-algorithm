#!/usr/bin/env python
# -*- coding: utf-8 -*-

__author__ = 'lina'
__date__ = '16/4/19'

# 赋值
will = ["Will", 28,  ["Python", "Java", "Go"]]
wilber = will
print id(will)
print will
print [id(ele) for ele in will]

print id(wilber)
print wilber
print [id(ele) for ele in wilber]

will[0] = "Wilber"
will[2].append("Lua")

print id(will)
print will
print [id(ele) for ele in will]

print id(wilber)
print wilber
print [id(ele) for ele in wilber]

# 浅拷贝
import copy

will = ["Will", 28,  ["Python", "Java", "Go"]]
wilber = copy.copy(will)
print id(will)
print will
print [id(ele) for ele in will]

print id(wilber)
print wilber
print [id(ele) for ele in wilber]

will[0] = "Wilber"
will[2].append("Lua")

print id(will)
print will
print [id(ele) for ele in will]

print id(wilber)
print wilber
print [id(ele) for ele in wilber]


# 深拷贝
import copy

will = ["Will", 28,  ["Python", "Java", "Go"]]
wilber = copy.deepcopy(will)
print id(will)
print will
print [id(ele) for ele in will]

print id(wilber)
print wilber
print [id(ele) for ele in wilber]

will[0] = "Wilber"
will[2].append("Lua")

print id(will)
print will
print [id(ele) for ele in will]

print id(wilber)
print wilber
print [id(ele) for ele in wilber]
