def find_duplicate(input_file='input_Day1.txt'):
    sum = 0
    seen = set([sum]) #returns a list with no duplicates
    freqs = [int(x) for x in open(input_file)] #split into list at new line (format of the input)
    while True:
        for n in freqs:
            sum += int(n) #add each number from the list to the freqs to the sum
            if sum in seen:
                return sum
            seen.add(sum)
    return seen


find_duplicates = find_duplicate()
print(f'The duplicate is {find_duplicates}')
