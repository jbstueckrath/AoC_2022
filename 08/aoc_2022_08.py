#!/usr/bin/env python3

import os
import numpy as np

workdir = os.getcwd()
#inputfile = "example_08.dat"
inputfile = "input_08.dat"


### first part ###

def get_parts(treemap, row, col):
    left = treemap[row][:col]
    right = treemap[row][col+1:]
    top = [treemap[r][col] for r in range(len(treemap))][:row]
    bottom = [treemap[r][col] for r in range(len(treemap))][row+1:]
    return [left, right, top, bottom]

def is_visible(treemap, row, col):
    height = treemap[row][col]
    parts = get_parts(treemap, row, col)
    is_visible = True
    if min([max(p) for p in parts]) >= height: is_visible = False
    return is_visible

with open(os.path.join(workdir, inputfile)) as inp:
    treedata = inp.read().splitlines()

treemap = []
for row in treedata: treemap.append([int(t) for t in row])
dim = len(treemap)

if not dim == len(treedata):
    print("Something went wrong reaing the input! Dimensionalities do not correspond.")
    exit()

no_trees_visible = dim*4 - 4
for row in range(dim)[1:-1]:
    for col in range(dim)[1:-1]:
        if is_visible(treemap, row, col): no_trees_visible += 1

print("The number of trees visible from the outside is {}.".format(no_trees_visible))


### second part ###

def get_no_visible_trees(part, height):
    no_visible_trees = 0
    for tree in part:
        no_visible_trees += 1
        if tree >= height: break
    return no_visible_trees

def get_scenic_score(treemap, row, col):
    if row in [0, len(treemap)-1] or col in [0, len(treemap)-1]: return 0
    height = treemap[row][col]
    parts = get_parts(treemap, row, col)
    for lt in [0, 2]: parts[lt].reverse()
    return np.prod([get_no_visible_trees(p, height) for p in parts])

max_scenic_score = 0
for row in range(dim)[1:-1]:
    for col in range(dim)[1:-1]:
        if get_scenic_score(treemap, row, col) > max_scenic_score: max_scenic_score = get_scenic_score(treemap, row, col)

print("The highest scenic score of any tree is {}.".format(max_scenic_score))

