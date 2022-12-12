#!/usr/bin/env python3

import os

workdir = os.getcwd()
#inputfile = "example_09_1.dat"
#inputfile = "example_09_2.dat"
inputfile = "input_09.dat"


### first part ###

encoding = {0: {-1: 'L', 1: 'R'}, 1: {-1: 'D', 1: 'U'}}
motions = {'L': [0, -1], 'R': [0, 1], 'D': [1, -1], 'U': [1, 1]}

def get_relation(pos, prev, this):
    relation = []
    for xy in range(2):
        if not pos[prev][xy] == pos[this][xy]:
            relation.append(encoding[xy][pos[prev][xy] - pos[this][xy]])
    if not relation: return 'overlap'
    else: return ' '.join(relation)

def get_directions_t(relpos, move_prev):
    if relpos == 'overlap' or move_prev is None: return None
    if len(move_prev) == 1:
        if move_prev in relpos.split(): return relpos
        else: return None
    else:
        if len(relpos) == 1:
            if relpos in move_prev.split(): return move_prev
            else: return None
        else:
            move = list(set(relpos.split()) & set(move_prev.split()))
            if not move: return None
            else: return ' '.join(move)

def move_object(obj, pos, directions):
    if directions is None: return
    for direction in directions.split():
        pos[obj][motions[direction][0]] += motions[direction][1]
    return

with open(os.path.join(workdir, inputfile)) as inp:
    motiondata = inp.read().splitlines()

moves = [(m.split()[0], int(m.split()[1])) for m in motiondata]

positions = {'h': [0, 0], 't': [0, 0]}
tail_visited = ['0,0']
for move in moves:
    for _ in range(move[1]):
        directions_t = get_directions_t(get_relation(positions, 'h', 't'), move[0])
        move_object('h', positions, move[0])
        move_object('t', positions, directions_t)
        tail_position = ','.join([str(p) for p in positions['t']])
        if tail_position not in tail_visited: tail_visited.append(tail_position)

print("The number of positions the tail visits at least once is {}.".format(len(tail_visited)))


### second part ###

# now: head is not 'h', but 0
positions = {i: [0, 0] for i in range(10)}
tail_visited = ['0,0']
for move in moves:
    for _ in range(move[1]):
        moves_subsequent = [move[0]]
        for t in range(9): moves_subsequent.append(get_directions_t(get_relation(positions, t, t+1), moves_subsequent[t]))
        for t in range(10): move_object(t, positions, moves_subsequent[t])
        tail_position = ','.join([str(p) for p in positions[9]])
        if tail_position not in tail_visited: tail_visited.append(tail_position)

print("The number of positions the tail (9) visits at least once is {}.".format(len(tail_visited)))

