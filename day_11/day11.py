import copy

input_lines = []
with open('example.txt', 'r') as file:
    line = file.readline()
    while line:
        input_lines.append(list(line.strip()))
        line = file.readline()

# . = floor
# L = empty seat
# # = occupied seat


# If a seat is empty (L) and there are no occupied seats adjacent to it, the seat becomes occupied.
# If a seat is occupied (#) and four or more seats adjacent to it are also occupied, the seat becomes empty.
# Otherwise, the seat's state does not change.

# CURRENT ERROR:
# program is currently not applying the rules to all seats simultainously
# for example in the first line the # at [0][3] should become a L because the 3 below and one to the left are occupied
# however the one to the left should also change 
# currently it is going one by one through the row so the second one does not change
# possible solution: create a new temp_row array that:
    # if the seat is a floor
        # push that onto array
        # if it is L or # apply rules and change as necessary 


def check_adjacent_seats(arr, row, col):
    current = arr[row][col]
    # if there are 4 or more occupied adjacent seats the seat becomes empty
    # count the number of occupied adjacent seats
    count = 0
    # temp row will replace the current row
    temp_row = []
    # loop over current row
    # if item is a floor push onto array
    # if item is a seat
        # apply rules accordingly
    # LOOK INTO MOVING THIS INTO THE MAIN FUNCTION AND REFACTOR IT TO USE THE CHECK ADJACENT METHOD 
    # NO NEEED TO REPEAT THIS SO MUCH
    for i in range(len(row)):
        # if the element is a floor
        if arr[row][i] == '.':
            # put it on the array and move on
            temp_row.append(arr[row][i])
        # if the element is an empty seat
        if arr[row][i] == 'L':
            # if there are no occupied adjacent seats
            # if the seat to the left exists and is occupied
            if col-1 > 0 and arr[row][col-1] == '#':

        # check if the seat has any occupied adjacent seats
        # if the seat to the left exists and is occupied
        if col-1 > 0 and arr[row][col-1] == '#':
            count += 1
        # check if the seat above exists and is occupied
        if row-1 > 0 and arr[row-1][col] == '#':
            count += 1
        # check the seat to the right exists and is occupied
        if col+1 < len(arr[row]) and arr[row][col+1] == '#':
            count += 1
        # check the seat below exists and is occupied
        if row+1 < len(arr) and arr[row+1][col] == '#':
            count += 1
        # check if the seat up left exists and is occupied
        if row-1 > 0 and col-1 > 0 and arr[row-1][col-1] == '#':
            count += 1
        # check if the seat up and right exists and is occupied
        if row-1 > 0 and col+1 < len(arr[row]) and arr[row-1][col+1] == '#':
            count += 1
        # check if the seat down and left exists and is occupied
        if row+1 < len(arr) and col-1 > 0 and arr[row+1][col-1] == '#':
            count += 1
        # check if the seat down and right exists and is occupied
        if row+1 < len(arr) and col+1 < len(arr[row]) and arr[row+1][col+1] == '#':
            count += 1
    return count

def find_final_seats(input):
    # input is a 2d array
    # the initial pass sets every open seat to occupied
    for row in range(len(input)):
        for col in range(len(input[row])):
            if input[row][col] == 'L':
                input[row][col] = '#'
    # diff will keep track if the array changes
    diff = True
    # make a deepcopy of the input array
    # using deepcopy copies the actual data rather than just creating a reference    
    arr_copy = copy.deepcopy(input)
    # now loop over the arr_copy and apply the rules until 
    while diff:
        for row in range(len(arr_copy)):
            for col in range(len(arr_copy[row])):
                # if a seat is empty ('L')
                curr_seat = arr_copy[row][col]
                if curr_seat == 'L':
                    # if there are no occupied adjacent seats
                    if check_adjacent_seats(arr_copy, row, col) == 0:
                        # the seat becomes occupied
                        # using curr_seat here doesnt update in the array
                        arr_copy[row][col] = '#'
                # if a seat is occupied
                if curr_seat == '#':
                    # and there are four or more occupied adjacent seats
                    if check_adjacent_seats(arr_copy, row, col) >= 4:
                        # the seat becomes empty
                        # using curr_seat here doesnt update in the array
                        arr_copy[row][col] = 'L'
        # after looping over arr_copy and applying the rules
        # make a copy and see if they are the same
        if arr_copy == (copy.deepcopy(arr_copy)):
            # set diff to false to break out of the loop
            diff = False
    # after the loop has finished
    # count how many occupied seats there are
    count = 0
    for row in range(len(arr_copy)):
        for col in range(len(arr_copy[row])):
            if arr_copy[row][col] == '#':
                count += 1
            else:
                continue
    print(count)


find_final_seats(input_lines)

# input.txt
# incorrect: 2026 (too low)
# example.txt -- target: 37
# incorrect: 43 (too high)