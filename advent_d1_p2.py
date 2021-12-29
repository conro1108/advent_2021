import sys 

inputFile = open("input_d1p1.txt")
input = [int(x) for x in inputFile.readlines()]

buffer = [input[0], input[1], input[2]]
exit_ptr = 0
transitions = {0:1, 1:2, 2:0}


increase_count = 0
old_sum = sum(buffer)

for measurement in input[3:]:
    buffer[exit_ptr] = measurement
    exit_ptr = transitions[exit_ptr]
    new_sum = sum(buffer)
    if new_sum > old_sum:
        increase_count += 1
    old_sum = new_sum

print(increase_count)
