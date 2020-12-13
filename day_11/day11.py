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

def check_adjacent_seats(arr, row, col):
    # keep track of occupied seats
    count = 0
    # check if the seat has any occupied adjacent seats
    # if the seat to the left exists and is occupied
    if col-1 != 0 and arr[row][col-1] == '#':
        count += 1
    # check if the seat above exists and is occupied
    elif row-1 != 0 and arr[row-1][col] == '#':
        count += 1
    # check the seat to the right exists and is occupied
    elif col+1 <= len(arr[row]) and arr[row][col+1] == '#':
        count += 1
    # check the seat below exists and is occupied
    elif row+1 <= len(arr) and arr[row+1][col] == '#':
        count += 1
    # check if the seat up left exists and is occupied
    elif row-1 > 0 and col-1 > 0 and arr[row-1][col-1] == '#':
        count += 1
    # check if the seat up and right exists and is occupied
    elif row-1 > 0 and col+1 < len(arr[row]) and arr[row-1][col+1] == '#':
        count += 1
    # check if the seat down and left exists and is occupied
    elif row+1 < len(arr) and col-1 > 0 and arr[row+1][col-1] == '#':
        count += 1
    # check if the seat down and right exists and is occupied
    elif row+1 < len(arr) and col+1 < len(arr[row]) and arr[row+1][col+1] == '#':
        count += 1
    return count

def find_final_seats(input):
    # input is a 2d array
    # the initial pass sets every open seat to occupied
    for row in range(len(input)):
        for col in range(len(input[row])):
            if input[row][col] == 'L':
                input[row][col] = '#'
    # now loop over the arr_copy and apply the rules until 
    while True:
        # make a deepcopy of the input array
        # using deepcopy copies the actual data rather than just creating a reference    
        arr_copy = copy.deepcopy(input)
        for row in range(len(arr_copy)):
            for col in range(len(arr_copy[row])):
                # if a seat is empty ('L')
                if arr_copy[row][col] == 'L':
                    # check if there are any occupied adjacent seats
                    if check_adjacent_seats(arr_copy, row, col) < 4:

















find_final_seats(input_lines)



# input is a 2d array
    # loop over the 2d array
    # for row in range(len(new_arr)):
    #     print(len(new_arr[row]))
        # for col in range(len(new_arr[row])):
            # check if the seat is empty
            # print(col)
            # if new_arr[row][col] == 'L':
                # print(new_arr[row][col])
                # has_empty_seats = check_adjacent_seats(new_arr, row, col)
                # if has_empty_seats:
                #     print('has empty seats')
                    # new_arr[row][col] = '#'