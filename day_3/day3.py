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
            # print(idx, len(i), i[idx], count)

        if(idx+3 >= len(i)-1):
            idx = (idx - len(i)) + 4
        else:
            idx += 3

    print(count)
    return count

def count_trees_part2(input, right, down):
    count = 0
    idx = 0
    for i in range(0, len(input), down):
        # print(i)
        if(input[i][idx] == '#'):
            count += 1
        if(idx+right >= len(input[i])-1):
            idx = (idx - len(input[i])) + (right+1)
        else:
            idx += right
    print(count)
    return count

run1 = count_trees_part2(lines, 1, 1)
run2 = count_trees_part2(lines, 3, 1)
run3 = count_trees_part2(lines, 5, 1)
run4 = count_trees_part2(lines, 7, 1)
run5 = count_trees_part2(lines, 1, 2)



# count_trees(lines)
count_trees_part2(lines, 3, 1)
print(run1*run2*run3*run4*run5)