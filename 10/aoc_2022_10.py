#!/usr/bin/env python3

import os

workdir = os.getcwd()
#inputfile = "example_10.dat"
inputfile = "input_10.dat"


### first part ###

def get_signal_strength(data, cycle):
    return cycle*data[cycle-1]

with open(os.path.join(workdir, inputfile)) as inp:
    programdata = inp.read().splitlines()

register = []
x = 1
for line in programdata:
    if line.split()[0] == 'noop': register.append(x)
    if line.split()[0] == 'addx':
        register.extend([x for _ in range(2)])
        x += int(line.split()[1])

strengths = [get_signal_strength(register, c) for c in range(20, 260, 40)]

print("The sum of the six signal strengths is {}.".format(sum(strengths)))


### second part ###

def draw(data, cycle):
    crt_pos = (cycle-1) % 40
    x = data[cycle-1]
    if crt_pos in [i for i in range(x-1, x+2)]: return '#'
    else: return '.'

image = [draw(register, c+1) for c in range(len(register))]

print("The program produces the following image:")
for l in range(len(register)//40): print(''.join(image[l*40:l*40+40]))

