#!/usr/bin/python3
import sys

maxCost = 0
maxKey = None

for line in sys.stdin:
    data_mapped = line.strip().split("\t")
    if len(data_mapped) != 2:
        # Something has gone wrong. Skip this line.
        continue

    thisKey, thisCost = data_mapped

    if float(thisCost) > maxCost:
        maxCost = float(thisCost)
        maxKey = thisKey
print(maxKey, "\t", maxCost)

