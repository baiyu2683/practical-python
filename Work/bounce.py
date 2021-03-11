#!/usr/bin/evn python3
# bounce.py
#
# Exercise 1.5
height = 100 # 米
bounce_per = 3 / 5
num = 1

while num <= 10:
    height *= bounce_per
    print(num, round(height, 4))
    num +=1 
