#!/usr/bin/env python3

import os
from copy import deepcopy

workdir = os.getcwd()
#inputfile = "example_14.dat"
inputfile = "input_14.dat"


### first part ###

def i2col(i):
    return i - min_col

def create_line(start, end):
    if start[0] == end[0]:
        row_s = min(start[1], end[1])
        row_e = max(start[1], end[1])
        for c in range(row_e - row_s + 1): cavemap[row_s+c][i2col(start[0])] = True
    if start[1] == end[1]:
        col_s = min(start[0], end[0])
        col_e = max(start[0], end[0])
        for c in range(col_e - col_s + 1): cavemap[start[1]][i2col(col_s+c)] = True
    return

def drop_sand():
    pos = {'row': 0, 'col': i2col(500)}
    for d in range(dim_row)[1:]:
        if not cavemap[d][pos['col']]: pos['row'] = d
        elif not cavemap[d][pos['col']-1]:
            pos['row'] = d
            pos['col'] -= 1
        elif not cavemap[d][pos['col']+1]:
            pos['row'] = d
            pos['col'] += 1
        else: break
    cavemap[pos['row']][pos['col']] = True

with open(os.path.join(workdir, inputfile)) as inp:
    mapdata = inp.read().splitlines()

rockdata = [[] for _ in range(len(mapdata))]
for l in range(len(mapdata)):
    for e in mapdata[l].split(' -> '): rockdata[l].append(tuple([int(i) for i in e.split(',')]))

min_col = min([min([rock[0] for rock in edges]) for edges in rockdata]) - 1
max_col = max([max([rock[0] for rock in edges]) for edges in rockdata]) + 1
dim_col = max_col - min_col + 1
dim_row = max([max([rock[1] for rock in edges]) for edges in rockdata]) + 2

cavemap = [[False for _ in range(dim_col)] for _ in range(dim_row)]
for edges in rockdata:
    for e in range(len(edges))[1:]: create_line(edges[e-1], edges[e])

sandflow = True
units = 0
while sandflow:
    drop_sand()
    if True in cavemap[-1]: sandflow = False
    else: units += 1

print("The number of sand units that come to rest before the overflow is {}.".format(units))


### second part ###

dim_row = max([max([rock[1] for rock in edges]) for edges in rockdata]) + 3
dim_col = 2*dim_row + 1
min_col = 500 - dim_row

cavemap = [[False for _ in range(dim_col)] for _ in range(dim_row)]
for edges in rockdata:
    for e in range(len(edges))[1:]: create_line(edges[e-1], edges[e])
cavemap[-1] = [True for _ in range(dim_col)]

units = 0
while not cavemap[0][i2col(500)]:
    drop_sand()
    units += 1

print("The number of sand units that come to rest before reaching the top is {}.".format(units))

