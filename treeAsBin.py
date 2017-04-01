# -*- coding: utf-8 -*-
"""
Created on Sept. 2016

@author: nb, gd
"""

class TreeAsBin:
    """
    Simple class for (General) Trees
    represented as Binary Trees (first child - right sibling)
    """

    def __init__(self, key, child=None, sibling=None):
        """
        Init Tree
        """
        self.key = key
        self.child = child
        self.sibling = sibling


def tutoEx1():
    C1 = TreeAsBin(3, TreeAsBin(-6, None, TreeAsBin(10)))
    C2 = TreeAsBin(8, TreeAsBin(11, TreeAsBin(0, None, TreeAsBin(4)),
                                TreeAsBin(2, None, TreeAsBin(5))))
    C3 = TreeAsBin(9)
    C1.sibling = C2
    C2.sibling = C3
    return TreeAsBin(15, C1, None)

# measures
#------------------------------------------------------------------------------

def size(B):
    s = 1
    C = B.child
    while C:
        s += size(C)
        C = C.sibling
    return s

def size2(B):
    if B == None:
        return 0
    else:
        return 1 + size2(B.child) + size2(B.sibling)


# height

def height(B):
    h = -1
    C = B.child
    while C:
        h = max(h, height(C))
        C = C.sibling
    return h + 1

def height2(B):
    if B == None:
        return -1
    else:
        return max(1 + height2(B.child), height2(B.sibling))

# External Path Length
def epl(B, h=0):
    if B.child:
        length = 0
        C = B.child
        while C:
            length += epl(C, h+1)
            C = C.sibling
        return length
    else:
        return h
