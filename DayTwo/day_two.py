# Advent of Code, 2024
# Day Two


with open("input.txt") as f:
    data = f.readlines()

def is_safe_row(row):
    if row == sorted(row) or row == sorted(row, reverse=True):
        if all(1 <= abs(row[i + 1] - row[i]) <= 3 for i in range(len(row) - 1)):
            return True
    return False

def is_safe_row_two(row):
    for i in range(len(row)):
        new_row = row[:i] + row[i + 1:]
        if is_safe_row(new_row):
            return True
    return False

# PART ONE
total1 = 0

for row_count in data:
    row = list(map(int, row_count.split()))

    if is_safe_row(row):
        total1 += 1

print(total1)

# PART TWO
total2 = 0

for row_count in data:
    row = list(map(int, row_count.split()))

    if is_safe_row(row):
        total2 += 1
    elif is_safe_row_two(row):
        total2 += 1

print(total2)
