#!/usr/bin/env python3

import os
import numpy as np
from copy import deepcopy

workdir = os.getcwd()
#inputfile = "example_13.dat"
inputfile = "input_13.dat"


### first part ###

def get_first(pair):
    left, right = pair
    for e in range(min(len(left), len(right))):
        # if both are lists: jump to next element or go one recursive level deeper
        if isinstance(left[e], list) and isinstance(right[e], list):
            if left[e] == right[e]: continue
            return get_first((left[e], right[e]))
        # if one is int, the other one is list: convert int to list and restart
        if isinstance(left[e], int) and isinstance(right[e], list):
            left[e] = [left[e]]
            return get_first(pair)
        if isinstance(left[e], list) and isinstance(right[e], int):
            right[e] = [right[e]]
            return get_first(pair)
        # if both int: check if one is higher
        if left[e] < right[e]: return 'left'
        if left[e] > right[e]: return 'right'
    # if end of list: check if one list is longer
    if len(left) < len(right): return 'left'
    if len(left) > len(right): return 'right'
    # if still nothin is return, you are stuck in the lowest recursive level
    # externally restart the search with the changed pair
    return 'stuck'

with open(os.path.join(workdir, inputfile)) as inp:
    listdata = inp.read().splitlines()

original_listpairs = []
for l in range(len(listdata)//3+1): original_listpairs.append((eval(listdata[l*3]), eval(listdata[l*3+1])))
listpairs = deepcopy(original_listpairs)

indexsum = 0
for index, pair in enumerate(listpairs):
    packet_first = get_first(pair)
    # this will be an infinite loop if left and right are identical
    while packet_first == 'stuck': packet_first = get_first(pair)
    if packet_first == 'left': indexsum += index + 1

print("The sum of the indices of the pairs in the right order is {}.".format(indexsum))


### second part ###

listpairs = deepcopy(original_listpairs)
packets = []
for pair in listpairs: packets.extend([pair[0], pair[1]])

# I dont't want to actually order everything, so just count elements before the identifiers
identifiers = [[[2]], [[6]]]
ident_counters = [0, 0]
for packet in packets:
    for ident in identifiers:
        packet_first = get_first((packet, ident))
        while packet_first == 'stuck': packet_first = get_first((packet, ident))
        if packet_first == 'left': ident_counters[identifiers.index(ident)] += 1

ident_indices = [count+i+1 for i, count in enumerate(ident_counters)]

print("The product of the indices of the identifiers is {}.".format(np.prod(ident_indices)))

