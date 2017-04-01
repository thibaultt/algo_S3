# -*- coding: utf-8 -*-
"""
Created on Sept. 2016

@author: nb, gd
"""

# General Tree class
# ------------------------------------------------------------------------------

class Tree:
    """
    Simple class for General Tree
    """

    def __init__(self, key, children=None):
        """
        Init General Tree, ensure children are properly set.
        """
        self.key = key
        if children is not None:
            self.children = children
        else:
            self.children = []

    @property
    def nbChildren(self):
        return len(self.children)





def tutoEx1():
    C1 = Tree(3, [Tree(-6), Tree(10)])
    C2 = Tree(8, [Tree(11, [Tree(0), Tree(4)]), Tree(2), Tree(5)])
    C3 = Tree(9)
    return Tree(15, [C1, C2, C3])


# measures
#------------------------------------------------------------------------------

def size(T):
    s = 1
    for i in range(T.nbChildren):
        s += size(T.children[i])
    return s

def height(T):
    h = -1
    for i in range(T.nbChildren):
        h = max(h, height(T.children[i]))
    return h + 1

# External Path Length
def epl(T, h=0):
    """
    External Path Length
    """
    if T.nbChildren > 0:
        length = 0
        for i in range(T.nbChildren):
            length += epl(T.children[i], h+1)
        return length
    else:
        return h
