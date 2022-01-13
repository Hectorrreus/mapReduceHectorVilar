#!/usr/bin/python3
import sys

maxCost = 0
oldKey = None

for line in sys.stdin:
    data_mapped = line.strip().split("\t")
    if len(data_mapped) != 2:
        # Something has gone wrong. Skip this line.
        continue

    thisKey, thisCost = data_mapped
    if oldKey and oldKey != thisKey:
        print(oldKey, "\t", maxCost)
        oldKey = thisKey   #sobra?? 
        maxCost = 0

    oldKey = thisKey
    if float(thisCost) > maxCost:
        maxCost = float(thisCost)

if oldKey != None:
    print(oldKey, "\t", maxCost)
