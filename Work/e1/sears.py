#!/usr/bin/env python3
bill_height = 0.00011 # m
sear_height = 442 # m
num_bills = 1
day = 1

print(day, num_bills, bill_height)
while bill_height * num_bills < sear_height:
    num_bills = num_bills * 2
    day += 1
    print(day, num_bills, bill_height * num_bills)

print('Number of bills:', num_bills)
print('Number of days:', day)
print('Final Height:', bill_height * num_bills)
