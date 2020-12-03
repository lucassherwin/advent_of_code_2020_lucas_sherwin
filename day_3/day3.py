input_txt = open('input.txt', 'r')
lines = input_txt.readlines()

# count all trees('#') you would encounter going right 3 down 1
def count_trees(input):
    # keep track of the number of trees encountered
    count = 0
    # keep track of toboggan position
    idx = 0 # start at the top left 
    for i in input:
        # check if the character at idx == #
        if(i[idx] == '#'):
            # increase count by 1
            count += 1
        # check if idx + 3 will be greater than len(i)
        if((idx+3) > (len(i)-1)):
            # if so, set idx to be the length - idx
            idx = (len(i))-idx
        # otherwise increment idx by 3
        else:
            idx += 3
        print(idx, len(i), i[idx], count)
    print(count)
    return count



count_trees(lines)
