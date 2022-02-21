#!/usr/bin/env python3

bill_thickness = 0.11 * 0.001
sears_tower_height = 442
num_bills = 1
day = 1

while num_bills * bill_thickness < sears_tower_height:
    num_bills = num_bills * 2
    day += 1

print("num_bills: ", num_bills)
print("day: ", day)
