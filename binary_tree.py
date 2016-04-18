#!/usr/bin/env python
# -*- coding: utf-8 -*-

__author__ = 'lina'
__date__ = '16/4/17'


class Node(object):

    def __init__(self, element=-1, lchild=None, rchild=None):
        self.element = element
        self.lchild = lchild
        self.rchild = rchild


class Tree(object):

    def __init__(self):
        self.root = Node()

    def add(self, element):

        node = Node(element)

        if self.root.element == -1:
            self.root = node

        else:
            my_queue = list()
            tree_node = self.root
            my_queue.append(tree_node)
            while my_queue:
                tree_node = my_queue.pop(0)
                if not tree_node.lchild:
                    tree_node.lchild = node
                    return
                if not tree_node.rchild:
                    tree_node.rchild = node
                    return
                else:
                    my_queue.append(tree_node.lchild)
                    my_queue.append(tree_node.rchild)

    def front_digui(self, root):

        if not root:
            return

        print root.element,

        self.front_digui(root.lchild)
        self.front_digui(root.rchild)

    def middle_digui(self, root):

        if not root:
            return

        self.middle_digui(root.lchild)
        print root.element,
        self.middle_digui(root.rchild)

    def later_digui(self, root):
        if not root:
            return

        self.later_digui(root.lchild)
        self.later_digui(root.rchild)
        print root.element,

    def front_stack(self, root):
        if not root:
            return

        mystack = []
        node = root
        while node or mystack:
            while node:
                print node.element,
                mystack.append(node)
                node = node.lchild

            node = mystack.pop()
            node = node.rchild

    def middle_stack(self, root):
        if not root:
            return

        mystack = []
        node = root
        while node or mystack:
            while node:
                mystack.append(node)
                node = node.lchild

            node = mystack.pop()
            print node.element,
            node = node.rchild

    def later_stack(self, root):
        if not root:
            return

        my_stack1 = list()
        my_stack2 = list()
        node = root
        my_stack1.append(node)
        while my_stack1:
            node = my_stack1.pop()
            if node.lchild:
                my_stack1.append(node.lchild)

            if node.rchild:
                my_stack1.append(node.rchild)

            my_stack2.append(node)

        while my_stack2:
            print my_stack2.pop().element,

    def level_queue(self, root):

        if not root:
            return

        my_queue = list()
        node = root
        my_queue.append(node)
        while my_queue:
            node = my_queue.pop(0)
            print node.element,
            if node.lchild:
                my_queue.append(node.lchild)
            if node.rchild:
                my_queue.append(node.rchild)

    def find_lca(self, root, node1, node2):

        if not root:
            return

        if root.element == node1 or root.element == node2:
            return root

        left_lca = self.find_lca(root.lchild, node1, node2)
        right_lca = self.find_lca(root.rchild, node1, node2)

        if left_lca and right_lca:
            return root
        if left_lca:
            return left_lca
        return right_lca


if __name__ == '__main__':
    elements = range(10)
    tree = Tree()
    for element in elements:
        tree.add(element)

    tree.level_queue(tree.root)
    print "\n"
    tree.front_digui(tree.root)
    print "\n"

    tree.front_stack(tree.root)

    print "\n"
    tree.middle_digui(tree.root)
    print "\n"

    tree.middle_stack(tree.root)

    print "\n"
    tree.later_digui(tree.root)
    print "\n"

    tree.later_stack(tree.root)

    a = tree.find_lca(tree.root, 5, 6)
    print a.element