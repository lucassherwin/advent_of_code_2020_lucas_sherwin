import math

with open('input.txt', 'r') as file:
    input_lines = file.readlines()

def find_seat_locations(input):
    # use to find the seat with the highest ID
    max_seat = 0
    for i in input:
        max_seat = max(max_seat, locate_seat(i.strip()))
    print(f'Part one answer {max_seat}')

def locate_seat(seat):
    # upper and lower bounds for the row and column
    upper_row = 127
    lower_row = 0

    upper_col = 7
    lower_col = 0

    for i in seat:
        # F means take the lower half EX: rows 0 - 63
        if i == 'F':
            # reassign upper bound
            upper_row -= math.ceil((upper_row - lower_row) / 2)
            # print(f'F means to take the lower half, keeping rows {lower_row} through {upper_row}.')
        # B means take the upper half EX: rows 32 - 63
        elif i == 'B':
            lower_row += math.ceil((upper_row - lower_row) / 2)
            # print(f'B means to take the upper half, keeping rows {lower_row} through {upper_row}.')
        # calculate columns
        # R means take the upper half
        elif i == 'R':
            lower_col += math.ceil((upper_col - lower_col) / 2)
            # print(f'R means to take the upper half, keeping columns {lower_col} through {upper_col}.')
        # L means take the lower half 
        else:
            upper_col -= math.ceil((upper_col - lower_col) / 2)
            # print(f'L means to take the lower half, keeping columns {lower_col} through {upper_col}.')

    # calculate the seat id
    seat_id = lower_row * 8 + lower_col
    return seat_id

# part 2
def find_seat(input):
    # store a list of all the seats
    seats = []
    for i in input:
        # get the seat location
        seats.append(locate_seat(i.strip()))
    # sort the list of seats
    seats = sorted(seats)
    # locate your seat
    for i in range(1, len(seats)-1):
        if(seats[i+1] - seats[i-1] != 2):
            print(f'Part two answer {seats[i]+1}')
            break
# locate_seat('FBFBBFFRLR')
find_seat_locations(input_lines)
find_seat(input_lines)