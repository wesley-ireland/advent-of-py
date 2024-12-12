import re

list1, list2 = [], []

with open('./day01_input.txt', 'r') as file:
    for line in file:
        pattern = re.compile(r'(?P<item1>\d+)\s+(?P<item2>\d+)')
        list1.append(int(pattern.match(line).group('item1')))
        list2.append(int(pattern.match(line).group('item2')))

appearanceMap = {}

for item in list2:
    if item in appearanceMap:
        appearanceMap[item] += 1
    else:
        appearanceMap[item] = 1

similarityScore = 0

for item in list1:
    if item in appearanceMap:
        similarityScore += item * appearanceMap[item]

print(similarityScore)
