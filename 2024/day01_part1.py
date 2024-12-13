import re
from file_utils import read_lines
lines = read_lines('./day01_input.txt')

list1, list2 = [], []

for line in lines:
    pattern = re.compile(r'(?P<item1>\d+)\s+(?P<item2>\d+)')
    list1.append(int(pattern.match(line).group('item1')))
    list2.append(int(pattern.match(line).group('item2')))

list1.sort()
list2.sort()

totalDistance = 0

for i in range(len(list1)):
    totalDistance += abs(list1[i] - list2[i])

print(totalDistance)
