# read the input file and create an array of ints
with open('day1_nums.txt', 'r') as file:
    input_lines = [int(line.strip()) for line in file]

# function to find two numbers in the list that add up to 2020
def findTwoNums(arr, sum):
    # sort the array
    arr.sort()
    #left and right indicies
    l = 0
    r = len(arr) - 1
    while(l < r):
        if(arr[l] + arr[r] == sum):
            # print the values
            print(arr[l], arr[r])
            # write the values to the output.txt file
            output = open('output.txt', 'w')
            output.write(f'{arr[l]} + {arr[r]} = 2020')
            output.write('\n')
            output.write(f'Total = {arr[l] * arr[r]}')
            output.close()
            return (arr[l] * arr[r])
        # if its less than the sum increment left pointer
        elif(arr[l] + arr[r] < sum):
            l += 1
        # otherwise decrement right pointer
        else:
            r -= 1
    return 0

# same problem and input but this time find 3 numbers that sum to 2020
def findThreeNums(arr, sum):
    # sort the array
    arr.sort()

    # start at beginning
    for i in range(0, len(arr)-2):
        # index of the first remaining element
        l = i + 1

        # index of the last element
        r = len(arr) - 1
        
        # same while loop
        while(l < r):
            if(arr[i] + arr[l] + arr[r] == sum):
                print(f'{arr[i]} + {arr[l]} + {arr[r]} = {sum}')
                output_2 = open('output_2.txt', 'w')
                output_2.write(f'{arr[i]} + {arr[l]} + {arr[r]} = {sum}')
                output_2.write('\n')
                output_2.write(f'Total = {arr[i] * arr[l] * arr[r]}')
                output_2.close()
                return (arr[i] * arr[l] * arr[r])
            elif (arr[i] + arr[l] + arr[r] < sum):
                # increment left
                l += 1
            else:
                r -= 1
    return 0



findTwoNums(input_lines, 2020)
findThreeNums(input_lines, 2020)

# https://adventofcode.com/2020/day/1