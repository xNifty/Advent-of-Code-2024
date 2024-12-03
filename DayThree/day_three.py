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

# Part Two
pattern = r"do\(\)|don't\(\)|mul\((\d+),\s*(\d+)\)"
count = 0

do = True

with open("input.txt") as f:
    for line in f:
        for match in re.finditer(pattern, line):
            if match.group() == "do()":
                do = True
            elif match.group() == "don't()":
                do = False
            elif do:
                count += int(match.group(1)) * int(match.group(2))

print(count)
