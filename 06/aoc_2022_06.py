#!/usr/bin/env python3

import os

workdir = os.getcwd()
#inputfile = "example_06.dat"
inputfile = "input_06.dat"


### first part ###

def is_unequal(word, noc):
    if len(word) != noc:
        print("ERROR: word {} does not have {} characters!".format(word, noc))
        exit()
    is_unequal = True
    for c in word:
        if word.count(c) > 1:
            is_unequal = False
            break
    return is_unequal

with open(os.path.join(workdir, inputfile)) as inp:
    stream = inp.readline().strip()

for i in range(len(stream)):
    if i in [j for j in range(3)]: continue
    if is_unequal(stream[i-3:i+1], 4):
        packet_index = i + 1
        break

print("The number of processed characters before the first start-of-packet marker is {}.".format(packet_index))


### second part ###

for i in range(len(stream)):
    if i in [j for j in range(13)]: continue
    if is_unequal(stream[i-13:i+1], 14):
        message_index = i + 1
        break

print("The number of processed characters before the first start-of-message marker is {}.".format(message_index))

