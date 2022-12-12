#!/usr/bin/env python3

import os

workdir = os.getcwd()
#inputfile = "example_04.dat"
inputfile = "input_04.dat"


### first part ###

def get_assignment(elf):
    start, end = elf.split('-')
    assignment = {i for i in range(int(start), int(end)+1)}
    return assignment

with open(os.path.join(workdir, inputfile)) as inp:
    elfpairdata = inp.readlines()

no_double_assignments = 0
no_overlap_assignments = 0   # belongs to second part
for elfpair in elfpairdata:
    elf_1, elf_2 = elfpair.split(',')
    assign_1 = get_assignment(elf_1)
    assign_2 = get_assignment(elf_2)
    if assign_1.issubset(assign_2) or assign_2.issubset(assign_1): no_double_assignments += 1
    if not assign_1.isdisjoint(assign_2): no_overlap_assignments += 1   # belongs to second part

print("The number of assignment pairs in which one fully contains the other is {}.".format(no_double_assignments))


### second part ###

print("The number of assignment pairs that overlap is {}.".format(no_overlap_assignments))

