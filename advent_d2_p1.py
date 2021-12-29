inputFile = open("input_d2p1.txt", "r")

# program state
x = 0
depth = 0

# define functions
def forward(dist):
    global x
    x += dist

def up(delta):
    global depth
    depth -= delta

def down(delta):
    global depth
    depth += delta

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