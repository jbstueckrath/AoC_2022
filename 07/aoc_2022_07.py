#!/usr/bin/env python3

import os

workdir = os.getcwd()
#inputfile = "example_07.dat"
inputfile = "input_07.dat"


### first part ###

def get_size_files(directory):
    return sum(directory['files'].values())

def get_size_total(directories, d):
    size = get_size_files(directories[d])
    if not directories[d]['dirs']:
        return size
    else:
        for subd in directories[d]['dirs']:
            size += get_size_total(directories, ';'.join([d, subd]))
        return size

with open(os.path.join(workdir, inputfile)) as inp:
    iodata = inp.read().splitlines()

# ATTENTION:
# In the input file, directory and file names can occur multiple times!
# Be careful to save a directory depending on the whole path.
# This is not the case in the example file.
directories = {'/': {'in': [], 'dirs': [], 'files': {}}}
currentdir = []

for index, io in enumerate(iodata):
    tmp = io.split()
    if tmp[0] != '$': continue

    if tmp[1] == 'cd':
        if tmp[2] == '..':
            currentdir = currentdir[:-1]
        else:
            currentdir.append(tmp[2])

    elif tmp[1] == 'ls':
        iadd = 1
        while(iodata[index + iadd].split()[0] != '$'):
            entry = iodata[index + iadd].split()
            if entry[0] == 'dir':
                directories[';'.join(currentdir)]['dirs'].append(entry[1])
                directories[';'.join(currentdir+[entry[1]])] = {'in': currentdir, 'dirs': [], 'files': {}}
            else:
                directories[';'.join(currentdir)]['files'][entry[1]] = int(entry[0])
            if (index + iadd + 1 == len(iodata)): break
            else: iadd += 1

final_size = 0
for d in directories.keys():
    size = get_size_total(directories, d)
    if size <= 100000: final_size += size

print("The total size of the directories with a maximum size of 100000 is {}.".format(final_size))


### second part ###

space_total = 70000000
space_needed = 30000000
space_used = get_size_total(directories, '/')
space_unused = space_total - space_used
space_needed_additional = space_needed - space_unused

possible_dirs = []
smallest = space_used
for d in directories.keys():
    space = get_size_total(directories, d)
    if space >= space_needed_additional:
        if space < smallest:
            smallest = space

print("The total size of the smallest directory needed to be deleted to get enough free space is {}.".format(smallest))

