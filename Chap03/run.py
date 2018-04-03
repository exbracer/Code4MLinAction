#!/usr/bin/env python
# coding=utf-8

import trees

myData, labels = trees.createDataSet()
print myData
myTree = trees.createTree(myData, labels)
print myTree
