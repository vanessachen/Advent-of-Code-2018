def frequency_changes(input_file='input_Day1.txt'):
    """Return the list of frequency changes given the input data"""
    return [int(line) for line in open(input_file)]

# Day 1 Part 1
freq_changes = frequency_changes()
f_c_sum = sum(freq_changes)
print(f'Sum is {f_c_sum}')


def find_duplicate(input_file='input_Day1.txt'):
    sum = 0
    seen = set([sum]) #returns a list with no duplicates
    while True:
        for n in freq_changes:
            sum += int(n) #add each number from the list to the freqs to the sum
            if sum in seen:
                return sum
            seen.add(sum)
    return seen

#Day 1 Part 2
find_duplicates = find_duplicate()
print(f'The duplicate is {find_duplicates}')
