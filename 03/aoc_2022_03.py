#!/usr/bin/env python3

import os

workdir = os.getcwd()
#inputfile = "example_03.dat"
inputfile = "input_03.dat"


### first part ###

def get_shared_item(rucksack):
    comp_1 = rucksack[:int(len(rucksack)/2)]
    comp_2 = rucksack[int(len(rucksack)/2):]
    shared_item = None
    for c in comp_1:
        if c in comp_2:
            shared_item = c
    if shared_item is None:
        print("No shared item found in rucksack {}!".format(rucksack))
        exit()
    return shared_item

def get_prio(item):
    if item.islower(): return ord(item) - 96     # 'a' is 97 and must give 1 (same for following letters)
    elif item.isupper(): return ord(item) - 38   # 'A' is 65 and must give 27 (same for following letters)

with open(os.path.join(workdir, inputfile)) as inp:
    rucksackdata = inp.read().splitlines()

prio_sum = 0
for rucksack in rucksackdata:
    shared_item = get_shared_item(rucksack)
    prio_sum += get_prio(shared_item)

print("The sum of the priorities of the shared items in all rucksacks is {}.".format(prio_sum))


### second part ###

def get_common_item(sack_1, sack_2, sack_3):
    common_item = None
    for c in sack_1:
        if (c in sack_2) and (c in sack_3):
            common_item = c
    if common_item is None:
        print("No common item found in rucksacks {}, {}, and {}!".format(sack_1, sack_2, sack_3))
        exit()
    return common_item

prio_sum = 0
for r in range(int(len(rucksackdata)/3)):
    common_item = get_common_item(rucksackdata[r*3], rucksackdata[r*3+1], rucksackdata[r*3+2])
    prio_sum += get_prio(common_item)


print("The sum of the priorities of the common items of all three-elf groups is {}.".format(prio_sum))

