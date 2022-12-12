#!/usr/bin/env python3

import os
from copy import deepcopy
import numpy as np

workdir = os.getcwd()
#inputfile = "example_11.dat"
inputfile = "input_11.dat"


### first part ###

class Monkey:

    def __init__(self, items, operation, test_division, test_true, test_false):
        self.items = items
        self.operator, self.operand = operation.split()
        self.test_division = test_division
        self.test_true = test_true
        self.test_false = test_false
        self.count_inspect = 0

    def get_worry_level(self, old_wl):
        if self.operator == '+':
            if self.operand == 'old': return old_wl*2
            else: return old_wl + int(self.operand)
        elif self.operator == '*':
            if self.operand == 'old': return old_wl**2
            else: return old_wl * int(self.operand)
        else:
            print("ERROR: Unknwon operator in class monkey!")
            exit()

    def is_divisible(self, num):
        if num % self.test_division == 0: return True
        else: return False

    def get_goal_monkey(self, worry_level):
        if self.is_divisible(worry_level): return self.test_true
        else: return self.test_false

    def do_inspect(self, is_part1):
        throws = []
        for item in self.items:
            self.count_inspect += 1
            worry_level = self.get_worry_level(item)
            if is_part1: worry_level //= 3
            else: worry_level %= prod_divisors
            throws.append((self.get_goal_monkey(worry_level), worry_level))
            self.items = self.items[1:]
        return throws

with open(os.path.join(workdir, inputfile)) as inp:
    monkeydata = inp.read().splitlines()

original_monkeys = []
for i, entry in enumerate(monkeydata):
    if not 'Monkey' in entry: continue
    original_monkeys.append(Monkey(
        [int(item.replace(',', '')) for item in monkeydata[i+1].split()[2:]],
        monkeydata[i+2][23:],
        int(monkeydata[i+3].split()[3]),
        int(monkeydata[i+4].split()[5]),
        int(monkeydata[i+5].split()[5])
    ))

monkeys = deepcopy(original_monkeys)
for _ in range(20):
    for monkey in monkeys:
        throws = monkey.do_inspect(is_part1=True)
        for throw in throws: monkeys[throw[0]].items.append(throw[1])

print("The level of monkey business after 20 rounds is {}.".format(np.prod(sorted([m.count_inspect for m in monkeys])[-2:])))


#### second part ###

monkeys = deepcopy(original_monkeys)
prod_divisors = np.prod([m.test_division for m in monkeys])
for _ in range(10000):
    for monkey in monkeys:
        throws = monkey.do_inspect(is_part1=False)
        for throw in throws: monkeys[throw[0]].items.append(throw[1])

print("The level of monkey business after 10000 rounds is {}.".format(np.prod(sorted([m.count_inspect for m in monkeys])[-2:])))

