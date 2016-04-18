#!/usr/bin/env python
# -*- coding: utf-8 -*-

__author__ = 'lina'
__date__ = '16/4/14'


class ListNode:

    def __init__(self, val):

        self.val = val
        self.next = None


def reverse(head):

    if not head:
        return

    if not head.next:
        return head

    cur = head
    pre = None
    result = None

    while cur:
        result = cur
        # bak = cur
        tmp = cur.next
        cur.next = pre
        pre = cur
        cur = tmp

    return result


def recurse(head, newhead):
    if not head:
        return
    if not head.next:
        return head

    else:
        newhead = recurse(head.next, newhead)
        head.next.next = head
        head.next = None

    return newhead

if __name__ == "__main__":
    l1 = ListNode(1)
    l2 = ListNode(2)
    l3 = ListNode(3)
    l4 = ListNode(4)
    l1.next = l2
    l2.next = l3
    l3.next = l4

    a = l1
    while a:
        print a.val
        a = a.next

    # new_a = recurse(l1, l4)
    # while new_a:
    #     print new_a.val
    #     new_a = new_a.next

    new = reverse(l1)
    while new:
        print new.val
        new = new.next




