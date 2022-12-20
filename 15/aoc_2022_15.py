#!/usr/bin/env python3

import os
import time

workdir = os.getcwd()
#inputfile = "example_15.dat"
inputfile = "input_15.dat"


### first part ###

class Sensor:

    def __init__(self, inputline):
        line = inputline.split()
        self.x = int(line[2].split('=')[1].replace(',', ''))
        self.y = int(line[3].split('=')[1].replace(':', ''))
        self.beacon_x = int(line[8].split('=')[1].replace(',', ''))
        self.beacon_y = int(line[9].split('=')[1])
        self.radius = abs(self.x - self.beacon_x) + abs(self.y - self.beacon_y)

    def get_contained_positions(self, row):
        distance = abs(self.y - row)
        width = 2*(self.radius - distance) + 1   # this is equal to 2*radius + 1 - 2*distance
        contained_positions = [p + self.x - self.radius + distance for p in range(width)]
        if self.beacon_y == row and self.beacon_x in contained_positions: contained_positions.remove(self.beacon_x)
        return contained_positions

    def is_in_range(self, pos):
        # for part 2
        distance = abs(pos[0]-self.x) + abs(pos[1]-self.y)
        if distance <= self.radius: return True
        else: return False

    def get_surroundings(self):
        # for part 2
        surroundings = []
        for y in range(self.y - self.radius - 1, self.y + self.radius + 2):
            if abs(y - self.y) > self.radius: surroundings.append((self.x, y))
            else:
                shift = self.radius - abs(y - self.y) + 1
                surroundings.extend([(self.x - shift, y), (self.x + shift, y)])
        return surroundings

def is_in_any_range(pos):
    # for part 2
    in_any_range = False
    for s in sensors:
        if s.is_in_range(pos):
            in_any_range = True
            break
    return in_any_range

with open(os.path.join(workdir, inputfile)) as inp:
    sensors = [Sensor(line) for line in inp.read().splitlines()]

desired_row = 2000000 if inputfile == "input_15.dat" else 10
positions = set()
for s in sensors: positions = positions.union(set(s.get_contained_positions(desired_row)))

print("In the row where y = {}, the number of positions that cannot contain a beacon is {}.".format(desired_row, len(positions)))


### second part ###

desired_dim = 4000000 if inputfile == "input_15.dat" else 20
distress_pos = None
possible = []
for s in sensors:
    for pos in s.get_surroundings():
        if pos[0] < 0 or pos[0] > desired_dim or pos[1] < 0 or pos[1] > desired_dim: continue
        if not is_in_any_range(pos):
            distress_pos = pos
            break
    if distress_pos is not None: break

print("The tuning frequency of the distress beacon is {}.".format(distress_pos[0]*4000000 + distress_pos[1]))
