# import itertools

with open('input.txt', 'r') as file:
    input_lines = [int(line.strip()) for line in file]

# find the first number in the list (after preamble) which is not the sum of two of the 25 numbers before it
# the number immediately after the preamble will be the sum of any 2 numbers in the preamble 

def find_num(input):
    # preamble start and end
    pre = input[0:25]

    # the number immediately after the preamble
    check_num = input[25]

    i = 0
    while i < len(pre):
        for j in pre:
            if pre[i] == j:
                continue
            # check if i + j = check_num
            elif pre[i] + j == check_num:
                # if so the number is good 
                # call the function recursively
                input = input[1 : len(input)]

                find_num(input)
            # no match is found meaning the number is bad
            elif i+1 > len(pre):
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



def part2(input, bad_num):
    # array holding the numbers to sum
    # will start out with only 2 numbers, then 3, then 4, etc
    # arr = []

    # j will be the number of additional numbers to check
    # range is the number of contiguous numbers to check
    # starts at 1 to check 2 numbers [i, range]
    digits = 1
    while digits < len(input):
        for i in range(len(input)-1):
            arr = input[i : digits]
            test_sum = sum(arr)

            if test_sum == bad_num:
                max_num = max(arr)
                min_num = min(arr)
                print(max_num + min_num)
                break
            else:
                continue
        digits += 1






part2(input_lines, 105950735)

# sums = set(map(sum, itertools.combinations(preamble, 2)))