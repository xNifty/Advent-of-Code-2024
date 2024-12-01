# Advent of Code 2024, Day 1

# PART ONE
# Read in the input file and split each line into two numbers, one on the left and one on the right
# From here, find difference between the two numbers, subtracting the smaller number from the larger
# and add to a running total sum value

with open('input.txt') as f:
    lines = f.readlines()

numbers_left = []
numbers_right = []

for line in lines:
    numbers = line.split(' ')
    numbers[3] = numbers[3].replace('\n', '')
    numbers_left.append(int(numbers[0]))
    numbers_right.append(int(numbers[3]))

numbers_left.sort()
numbers_right.sort()

differences = []

for i in range(len(numbers_left)):

    if numbers_left[i] > numbers_right[i]:
        difference = numbers_left[i] - numbers_right[i]
    else:
        difference = numbers_right[i] - numbers_left[i]

    differences.append(difference)

sum = 0
for i in differences:
    sum += i

print("Sum of differences (part one): ", sum)

# PART TWO
# For each number in left list, if it appears in the right list, for each time it appears
# multiple the left number by the amount of times it appears in right list and add to a running
# total sum value

sum = 0

for i in range(len(numbers_left)):
    if numbers_left[i] in numbers_right:
        sum += numbers_left[i] * numbers_right.count(numbers_left[i])

print("Sum of multiples (part two): ", sum)
