import re

with open('input.txt', 'r') as file:
    input_lines = [line.strip() for line in file]
    # print(input_lines)

def day2(input):
    # count to track the number of valid passwords
    count = 0

    #write solution to file
    output = open('output.txt', 'w')

    for i in input:
        # arr[0] is the policy and arr[1] is the password
        arr = i.replace(" ", "").split(':')
        policy = arr[0]
        password = arr[1]

        # isolate the numbers in policy
        bounds = re.sub("[^0-9]", " ", policy).strip().split(" ")
        # upper and lower bounds for how many times the letter has to appear in the password
        lower = int(bounds[0])
        upper = int(bounds[1])
        
        # isolate the letter in policy
        letter = re.sub(r'[^A-Za-z]', '', policy)
        

        # check if letter appears in password at least 'lower' times and at most 'upper' times
        if(password.count(letter) <= upper and password.count(letter) >= lower):
            count += 1
            output.write(f'{password} is valid\n')
    output.write(f'There are {count} valid passwords')
    output.close()
    print(count)
    return count

def day2_part2(input):
    count = 0 # track the number of valid passwords
    
    # output
    output = open('output_part2.txt', 'w')

    for i in input:
        # from the first part
        # arr[0] is the policy and arr[1] is the password
        arr = i.replace(" ", "").split(':')
        policy = arr[0]
        password = arr[1]

        # isolate the numbers in policy
        bounds = re.sub("[^0-9]", " ", policy).strip().split(" ")
        # upper and lower bounds for how many times the letter has to appear in the password
        lower = int(bounds[0])
        upper = int(bounds[1])
        
        # isolate the letter in policy
        letter = re.sub(r'[^A-Za-z]', '', policy)

        if(bool(password[lower-1] == letter) ^ bool(password[upper-1] == letter)):
            count += 1
            # output.write(f'{password} is valid\n')
    output.write(f'There are {count} valid passwords')
    output.close()
    print(count)
    return count

# day2(input_lines)
day2_part2(input_lines)