from file_utils import read_lines
reports = read_lines('./day02_input.txt')

num_safe_reports = 0


def is_all_gradual(levels):
    return all(1 <= abs(levels[i] - levels[i + 1]) <= 3 for i in range(len(levels) - 1))


def is_all_increasing_or_decreasing(levels):
    if len(levels) <= 2:
        return True
    all_increasing = all(levels[i] < levels[i + 1] for i in range(len(levels) - 1))
    all_decreasing = all(levels[i] > levels[i + 1] for i in range(len(levels) - 1))
    return all_increasing or all_decreasing


def is_safe(levels):
    return is_all_increasing_or_decreasing(levels) and is_all_gradual(levels)


for report in reports:
    levels = list(map(int, report.split(' ')))
    if is_safe(levels):
        num_safe_reports += 1
        continue
    for i in range(len(levels)):
        subset = levels[:i] + levels[i+1:]
        if is_safe(subset):
            num_safe_reports += 1
            break

print(num_safe_reports)
