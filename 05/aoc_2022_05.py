#!/usr/bin/env python3

import os
from copy import deepcopy

workdir = os.getcwd()
#inputfile = "example_05.dat"
inputfile = "input_05.dat"


### first part ###

def move_onebyone(configuration, amount, origin, target):
    for _ in range(amount): configuration[target].append(configuration[origin].pop(-1))

with open(os.path.join(workdir, inputfile)) as inp:
    cratedata = inp.readlines()

index_blank = None
movedata = []
for index, line in enumerate(cratedata):
    if line == '\n': index_blank = index
    if index_blank is not None and index > index_blank:
        tmp = line.split()
        movedata.append({
            'amount': int(tmp[1]),
            'origin': int(tmp[3]),
            'target': int(tmp[5])
        })

if index_blank is None:
    print("No blank line found in input file!")
    exit()

no_stacks = len(cratedata[index_blank - 1].split())
configuration_original = {stack+1: [] for stack in range(no_stacks)}
for index in reversed(range(index_blank - 1)):
    for stack in range(no_stacks):
        crate = cratedata[index][stack*4+1]
        if crate.isalpha(): configuration_original[stack+1].append(crate)
configuration = deepcopy(configuration_original)

for step in movedata: move_onebyone(configuration, step['amount'], step['origin'], step['target'])

message = ''
for cratelist in configuration.values(): message += cratelist[-1]

print("The final message (crates on top of the stacks) after one-by-one movement is {}.".format(message))


### second part ###

def move_simultaneously(configuration, amount, origin, target):
    configuration[target].extend(configuration[origin][-amount:])
    for _ in range(amount): configuration[origin].pop(-1)

configuration = deepcopy(configuration_original)
for step in movedata: move_simultaneously(configuration, step['amount'], step['origin'], step['target'])

message = ''
for cratelist in configuration.values(): message += cratelist[-1]

print("The final message (crates on top of the stacks) after simultaneous movement is {}.".format(message))

