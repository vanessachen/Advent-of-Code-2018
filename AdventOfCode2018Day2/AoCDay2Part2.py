def returnIDs(input_file='input_Day2.txt'):
    return [line for line in open(input_file)]

# Day 2 Part 1
IDs = returnIDs()

def find_common_letters():

     for id, ID1 in enumerate(IDs): #enumerate allows us to loop over something and have an automatic counter
         for ID2 in IDs[id+1:]:
             diff_indexes = []
             # note: All inputs have the same length
             for i in range(len(ID1)): #loop through each ID
                 if ID1[i] != ID2[i]: #if the i'th character of the next ID is not the same as the i'th char of the current ID
                     diff_indexes.append(i) #add index to list
                 if len(diff_indexes) > 1: #break loop if 1 char is off
                     break
             else:
                 if len(diff_indexes) == 1: #if the difference is off by exactly 1 character
                     #return from beginning to the different index, skip that, then diff index to the end
                     return ID1[:diff_indexes[0]] + ID1[diff_indexes[0]+1:]

common_letters = find_common_letters()
print(f'The common sequence is {common_letters}')
