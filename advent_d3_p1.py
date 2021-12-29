inputFile = open("input_d3p1.txt", "r")
input = [x.strip() for x in inputFile.readlines()]
wordLength = len(input[0])

one_counts = [0 for x in range(0, wordLength)]
zero_counts = [0 for x in range(0, wordLength)]

for line in input:
    for idx, char in enumerate(line):
        if char == '1':
            one_counts[idx] = one_counts[idx] + 1
        else:
            zero_counts[idx] = zero_counts[idx] + 1

def check(idx):
    return one_counts[idx] >= zero_counts[idx]

# lmfao
gamma = int("".join(
        ["1" if check(x) else "0" for x in range(0, wordLength)]
    ), 2)

epsilon = int("".join(
        ["0" if check(x) else "1" for x in range(0, wordLength)]
    ), 2)

print(epsilon * gamma)