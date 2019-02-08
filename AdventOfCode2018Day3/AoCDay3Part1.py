import numpy as np

def getInputs(input_file='input_Day3.txt'):
    return [line for line in open(input_file)]

# Day 3 Part 1
IDs = getInputs()

def get_claim(line):
    '''
    >>> test = "#1 @ 49,222: 19x20"
    >>> test.split()
    ['#1', '@', '49,222:', '19x20']
    '''
    _, _, border_dist, dim = line.split() #splits each line ID into above
    #go through border_dist and skip colon, and convert to integer instead of keeping as a string
    left_dist, top_dist = [int(d) for d in border_dist[:-1].split(",")]
    width, height = [int(x) for x in dim.split("x")] #same idea for width and height
    #top_dist = min in x-distance, top_dist + height = max in x-distance (that the rectangle takes over)
    #used to see location the rectangle takes over
    return (top_dist, top_dist + height, left_dist, left_dist + width)

def find_overlap():
    fabric = np.zeros((1000, 1000)) #create large fabric of 0's
    for line in IDs: #loop through every line of the input
        xmin, xmax, ymin, ymax = get_claim(line)
        fabric[xmin:xmax, ymin:ymax] += 1 #increment for a location on the array every time there is something there
    return np.count_nonzero(fabric > 1) #count the number of nonzero values to see how much overlap there is

overlap = find_overlap()
print(f'The number of squares that have been overlapped is {overlap}')
