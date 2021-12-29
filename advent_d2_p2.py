inputFile = open("input_d2p1.txt", "r")

# program state
x = 0
depth = 0
aim = 0

# define functions
def forward(dist):
    global x, depth
    x += dist
    depth += aim * dist

def up(delta):
    global aim
    aim -= delta

def down(delta):
    global aim
    aim += delta

# map functions to input strings
actions = {
    "forward" : forward,
    "down" : down,
    "up" : up
}

for line in inputFile.readlines():
    tokens = line.split(" ")
    # pass command value to function mapped to command
    actions[tokens[0]](int(tokens[1]))

print(x * depth)