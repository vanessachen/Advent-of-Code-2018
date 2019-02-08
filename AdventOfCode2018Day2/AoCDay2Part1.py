from collections import Counter #support convenient and rapid tallies

def returnIDs(input_file='input_Day2.txt'):
    return [line for line in open(input_file)]

# Day 2 Part 1
IDs = returnIDs()

def find_checksum():
    twos = 0
    threes = 0
    #for line in s.splitlines():
    for line in IDs:
        count = Counter(line.strip()) # Counter = dict subclass for counting hashable objects; 
        if 2 in count.values(): #if something occurs in a line twice
            twos += 1
        if 3 in count.values(): #if something occurs in a line three times
            threes += 1
    return twos * threes

checksum = find_checksum()
print (f'The checksum is {checksum}')
