#!/usr/bin/env python3

import os

workdir = os.getcwd()
#inputfile = "example_12.dat"
inputfile = "input_12.dat"


### first part ###

def get_height_char(hill):
    if hill == 'S': return 1
    elif hill == 'E': return 26
    else: return ord(hill) - 96

def get_height_pos(pos):
    return heightmap[pos[0]][pos[1]]

def get_neighbors(pos):
    height_ranges = [len(heightmap), len(heightmap[0])]
    neighborlist = []
    for xy in range(2):
        for change in [-1, 1]:
            neighbor = list(pos)
            if neighbor[xy] + change in range(height_ranges[xy]):
                neighbor[xy] += change
                neighborlist.append(tuple(neighbor))
    return neighborlist

def search_paths(pathtree):
    end_reached = False
    shell = -1
    while not end_reached:
        shell += 1
        neighbors = []
        for coord in pathtree[shell]:
            tmp_neighs = get_neighbors(coord)
            for neigh in tmp_neighs:
                if neigh not in neighbors and get_height_pos(coord)+1 >= get_height_pos(neigh): neighbors.append(neigh)
        pathtree.append(neighbors)
        if pos_end in neighbors: end_reached = True

with open(os.path.join(workdir, inputfile)) as inp:
    hilldata = inp.read().splitlines()

heightmap = []
for i, line in enumerate(hilldata):
    if 'S' in line: pos_start = (i, hilldata[i].index('S'))
    if 'E' in line: pos_end = (i, hilldata[i].index('E'))
    heightmap.append([get_height_char(h) for h in line])

pathtree = [[pos_start]]
search_paths(pathtree)

print("The fewest steps required to reach the location with the best signal from the start is {}.".format(len(pathtree)-1))


### second part ###

# now start with list of all positions with height a (1)
pathtree = [[]]
for row in range(len(heightmap)):
    for col in range(len(heightmap[0])):
        if heightmap[row][col] == 1: pathtree[0].append((row, col))
search_paths(pathtree)

print("The fewest steps required to reach the location with the best signal from any point with elevation a is {}.".format(len(pathtree)-1))

