with open('example.txt', 'r') as file:
    input_lines = file.readlines()

# find the first number in the list (after preamble) which is not the sum of two of the 25 numbers before it
# the number immediately after the preamble will be the sum of any 2 numbers in the preamble 

# STEPS:
    # 1. get preamble (starts as 0-24)
    # check if [25] is the sum of any 2 numbers in preamble
    # if so:
        # increase preamble start and end by 1 and check next number
    # otherwise:
        # return the bad number

def find_num(input):
    # preamble start and end
    # start = 0
    # end = 24
    pre = input[0:4]

    # the number immediately after the preamble
    check_num = input[5]
    for i in range(len(pre)-1):
        j = i + 1
        
        
        # check if i + j == check_num
        # indicating that the number is good
        if pre[i] + pre[j] == check_num:
            input = input[1:len(input)]

            # call the function with new input
            find_num(input)
        # found the bad number
        elif pre[i] == len(pre):
            print('bad: ', check_num)
    # print('asdf')
    return check_num




find_num(input_lines)