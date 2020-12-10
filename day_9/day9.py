with open('input.txt', 'r') as file:
    input_lines = [int(line.strip()) for line in file]

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
    pre = input[0:25]

    # the number immediately after the preamble
    # print(input)
    check_num = input[25]



    i = 0
    while i < len(pre):
        for j in pre:
            # if i and j are the same
            # print( 'pre[i]', pre[i], "check_num", check_num)
            # print('new -----------------')
            # print(input)
            # print(pre)
            # print('i', i, 'j', j, 'check_num', check_num)
            # print(pre[i])
            # print('-----------------')

            if pre[i] == j:
                # print('skip!')
                # print(input)
                continue
            # check if i + j = check_num
            elif pre[i] + j == check_num:
                # if so the number is good 
                # call the function recursively
                # print('pre[i]', pre[i], 'j', j, 'check_num', check_num)
                input = input[1 : len(input)]
                # print(input)
                # print('call again')
                find_num(input)
            # no match is found meaning the number is bad
            elif i+1 > len(pre):
                # print(input)
                print('found: ', check_num)
                return check_num
        i += 1
    print('bad: ', check_num)
    raise Exception('bad: ', check_num)
    # return check_num


try:
    find_num(input_lines)
except:
    pass

# incorrect: 4