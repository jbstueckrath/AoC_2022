#!/usr/bin/env python3

import os

workdir = os.getcwd()
#inputfile = "example_02.dat"
inputfile = "input_02.dat"


### first part ###

def get_points_choice(choice):
    if choice == 'X': return 1
    elif choice == 'Y': return 2
    elif choice == 'Z': return 3
    else:
        print("Invalid choice {}! (must be X, Y or Z)".format(choice))
        exit()

def get_points_outcome(choice_op, choice_me):
    if (choice_op == 'A' and choice_me == 'Y') or (choice_op == 'B' and choice_me == 'Z') or (choice_op == 'C' and choice_me == 'X'): return 6
    elif (choice_op == 'A' and choice_me == 'Z') or (choice_op == 'B' and choice_me == 'X') or (choice_op == 'C' and choice_me == 'Y'): return 0
    elif (choice_op == 'A' and choice_me == 'X') or (choice_op == 'B' and choice_me == 'Y') or (choice_op == 'C' and choice_me == 'Z'): return 3
    else:
        print("Something is wrong with the choice of the opponent ({}) and/or my choice ({})!".format(choice_op, choice_me))
        exit()

with open(os.path.join(workdir, inputfile)) as inp:
    stratdata = inp.readlines()

mypoints = 0
for game in stratdata:
    choices = game.split()
    mypoints += get_points_choice(choices[1]) + get_points_outcome(choices[0], choices[1])

print("Following the strategy guide exactly, my total score is {}.".format(mypoints))


### second part ###

def get_choice(choice_op, outcome):
    if choice_op not in ['A', 'B', 'C']:
        print("Something is wrong with the choice of the opponent ({})!".format(choice_op))
        exit()
    if outcome not in ['X', 'Y', 'Z']:
        print("Something is wrong with the desired outcome ({})!".format(outcome))
        exit()
    if outcome == 'X':
        if choice_op == 'A': return 'Z'
        elif choice_op == 'B': return 'X'
        elif choice_op == 'C': return 'Y'
    elif outcome == 'Y':
        if choice_op == 'A': return 'X'
        elif choice_op == 'B': return 'Y'
        elif choice_op == 'C': return 'Z'
    elif outcome == 'Z':
        if choice_op == 'A': return 'Y'
        elif choice_op == 'B': return 'Z'
        elif choice_op == 'C': return 'X'

mypoints = 0
for game in stratdata:
    gamedata = game.split()
    mychoice = get_choice(gamedata[0], gamedata[1])
    mypoints += get_points_choice(mychoice) + get_points_outcome(gamedata[0], mychoice)

print("Following the strategy guide correctly, my total score is {}.".format(mypoints))

