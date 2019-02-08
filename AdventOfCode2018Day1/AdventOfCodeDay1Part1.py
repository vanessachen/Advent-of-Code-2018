def frequency_changes(input_file='input_Day1.txt'):
    """Return the list of frequency changes given the input data"""
    return [int(line) for line in open(input_file)]

# Day 1 Part 1
freq_changes = frequency_changes()
f_c_sum = sum(freq_changes)
print(f'Sum is {f_c_sum}')
