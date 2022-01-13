#!/usr/bin/python3
import sys

totalCost = 0
maxKey = None

for line in sys.stdin:
    data_mapped = line.strip().split("\t")
    if len(data_mapped) != 2:
        # Something has gone wrong. Skip this line.
        continue

    thisKey, thisCost = data_mapped

    totalCost += float(thisCost)
print("Total de vendas: ", totalCost)
