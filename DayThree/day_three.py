# Advent of Code, 2024
# Day Three

import re

# Part One

pattern = r"mul\((\d+),\s*(\d+)\)"
data = []

with open("input.txt") as f:
    data = [
        int(match[0]) * int(match[1])
        for line in f
        for match in re.findall(pattern, line)
    ]

count = 0

for num in data:
    count += num

print(count)
