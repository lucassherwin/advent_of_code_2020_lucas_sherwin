# example.txt
# larger_example.txt
# input.txt

import itertools

with open('input.txt', 'r') as file:
    input_lines = [int(line.strip()) for line in file]

def test_adapters(input):
    # first add 0 onto the array to account for the initial charge from the outlet
    input.append(0)
    # sort the array
    input.sort()

    # keep track of the numbers with either a 1 jolt diff or a 3 jolt diff
    one_diff = 0
    three_diff = 1

    # for part 2
    # array that keeps track of all the elements that fall into these categories
    arr = []

    for i in range(len(input)-1):
        if input[i] + 3 == input[i+1]:
            three_diff += 1
            arr.append(input[i])
        # ignore 2 jolt difference
        elif input[i] + 2 == input[i+1]:
            arr.append(input[i])
            continue
        elif input[i] + 1 == input[i+1]:
            one_diff += 1
            arr.append(input[i])
    ans = one_diff * three_diff
    # max = max(input)
    print(ans)
    return arr



def part2(input):
    # gets all of the valid adapters
    nums = test_adapters(input)
    # total = itertools.combinations(nums)
    total = itertools.combinations(nums, len(nums))
    print(len(list(total)))






test_adapters(input_lines)

part2(input_lines)