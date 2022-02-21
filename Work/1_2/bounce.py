#!/usr/bin/env python3

height = 100  # meter
count = 1

while count <= 10:
    height = height * 3 / 5
    print(count, round(height, 4))
    count += 1
