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


def remove_duplicate(head):
    # input    1->2->3->3->3->4->4->5
    # output   1->2->3->4->5
    if not head:
        return

    if not head.next:
        return head

    node = head

    while head.next:
        if head.next.val == head.val:
            head.next = head.next.next
        else:
            head = head.next

    return node


def remove_duplicate_no_sort(head):

    # input 1->3->5->4->3->2->5
    # output 1->3->5->4->2

    if not head or not head.next:
        return head

    node = head
    node_val = list()

    node_val.append(head.val)

    while head.next:
        if head.next.val in node_val:
            if head.next.next:
                head.next = head.next.next
            else:
                head.next = None
            continue

        head = head.next

        if head:
            node_val.append(head.val)

    return node


def remove_all_duplicate(head):
    # input    1->2->3->3->4->4->5
    # output   1->2->5
    if not head:
        return

    if not head.next:
        return head

    # node = head
    node = ListNode(0)
    node.next = head

    head = node

    dup_val = -1

    while head.next and head.next.next:

        if head.next.val == head.next.next.val:
            dup_val = head.next.val
            if head.next.next.next:
                head.next = head.next.next.next
        elif head.next.val == dup_val:
            head.next = head.next.next

        else:
            head = head.next

    return node.next

if __name__ == "__main__":
    l1 = ListNode(1)
    l1_1 = ListNode(3)
    l2 = ListNode(5)
    l3 = ListNode(4)
    l4 = ListNode(3)
    l4_1 = ListNode(2)
    l4_2 = ListNode(3)
    l5 = ListNode(5)
    l1.next = l1_1
    l1_1.next = l2
    l2.next = l3
    l3.next = l4
    l4.next = l4_1
    l4_1.next = l4_2
    l4_2.next = l5

    # a = l1
    # while a:
    #     print a.val
    #     a = a.next
    #
    # # new_a = recurse(l1, l4)
    # # while new_a:
    # #     print new_a.val
    # #     new_a = new_a.next
    #
    # new = reverse(l1)
    # while new:
    #     print new.val
    #     new = new.next
    #
    # a = remove_duplicate(l1)
    # while a:
    #     print a.val
    #     a = a.next

    # a = remove_all_duplicate(l1)
    # while a:
    #     print a.val
    #     a = a.next

    a = remove_duplicate_no_sort(l1)
    while a:
        print a.val
        a = a.next




