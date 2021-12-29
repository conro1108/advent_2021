inputFile = open("input_d3p1.txt", "r")
input = [x.strip() for x in inputFile.readlines()]

# find most common bit at index n of list l
def most_common(l, n):
    one_count = 0
    for i in l:
        if i[n] == "1":
            one_count += 1
    return 1 if one_count >= len(l) - one_count else 0



# subset of list which has x as it's n-th digit
def process(l, n, x):
    common = most_common(l, n)
    rare = 1 - common
    filtered = list(filter(lambda z: z[n] == (str(common) if x else str(rare)), l))

    if len(filtered) == 1:
        return int(filtered[0], 2)
    elif len(filtered) > 1:
        return process(filtered, n+1, x)
    else:
        return -1

oxygen = process(input, 0, True)
print(oxygen)
co2 = process(input, 0, False)
print(co2)

print(oxygen * co2)