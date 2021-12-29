# advent_d1_p1
import sys 

inputFile = open("input_d1p1.txt")
input = [int(x) for x in inputFile.readlines()]

curr = sys.maxsize * 2
increase_count = 0

for measurement in input:
    if measurement > curr:
        increase_count += 1
    curr = measurement

print(increase_count)
