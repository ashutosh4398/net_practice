"""
program to count frequency of target at each level present in inputs
inputs can be nested lists

eg: input: [1,1,1,[2,2,3,1, [1,1,1,1, [5, 1]]], 1, [1]], target: 1
    output: [[0, 4], [1, 2], [2, 4], [3, 1]]
    at level 0, count =4
    at level 1, count=2
    at level 2, count=4
    at level 3, count=1
"""

from typing import List


def freq_count(inputs: List[List[int]], target: int, output=None, level: int = 0):
    if output is None:
        output = []
    count = 0
    for each in inputs:
        if isinstance(each, list):
            freq_count(each, target, output, level + 1)
        if each == target:
            count += 1

    updates = False
    for op in output:
        if op[0] == level:
            updates = True
            op[1] = op[1] + count
    if not updates:
        output.append([level, count])
    return sorted(output, key=lambda x: x[0])

l1 = [1,1,1,[2,2,3,1, [1,1,1,1, [5, 1]]], 1, [1]]
print(freq_count(l1, 1))