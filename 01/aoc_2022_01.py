#!/usr/bin/env python3

import os

workdir = os.getcwd()
#inputfile = "example_01.dat"
inputfile = "input_01.dat"


### first part ###

with open(os.path.join(workdir, inputfile)) as inp:
    fooddata = inp.readlines()

calories_list = []
calories = 0
for food in fooddata:
    tmp = food.split()
    if len(tmp) == 1:
        calories += int(tmp[0])
    elif len(tmp) == 0:
        calories_list.append(calories)
        calories = 0
    else:
        print("Something is wrong, check the code!")
        exit()

print("The elf carrying the most calories carries {} calories.".format(max(calories_list)))


### second part ###

calories_list.sort(reverse=True)

print("The top three elves carrying the most calories carry a total number of {} calories.".format(sum(calories_list[:3])))

