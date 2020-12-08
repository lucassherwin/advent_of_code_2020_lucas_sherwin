# import re

# with open('input.txt', 'r') as file:
#     input_lines = file.readlines()

# bags_count = 0

# # list of all bags
# bags = {}

# def how_many_bags(input):
#     for i in input:
#         rule = i.strip().split('contain')
#         print('rule', rule)
#         bag_key = rule[0].strip().replace('bags', '') 
#         # store the bags that can be put into the current bag key
#         val_bags = {}
#         print('bag_key', bag_key)

#         if 'no' in rule[1]:
#             print('no', rule[1])
#             val_bags = 0
#         else:
#             for t in [item.strip() for item in rule[1].split(',')]:
#                 temp_bag_num = t[0]
#                 temp_bag_key = re.sub(r'[0-9]+', '', t).replace('bags', '').replace('.', '').strip()
#                 print('temp_bag_num', temp_bag_num, 'temp_bag_key', temp_bag_key)
#                 val_bags[temp_bag_key] = temp_bag_num
#         bags[bag_key] = val_bags

#     for outer_bag in bags.keys():
#         if bags[outer_bag] != 0:
#             try:
#                 check_bag(bags[outer_bag])
#             except:
#                 continue

# # recursive function
# def check_bag(bag):
#     global bags_count

#     for bag_name, bag_val in bag.items():
#         # if we reach a shiny gold bag break out of function and move to next outer_bag
#         if bag_name == 'shiny gold':
#             bags_count += 1
#             raise Exception('Found path')
#         elif bags[bag_name] != 0:
#             check_bag(bags[bag_name])
#         else:
#             continue


# how_many_bags(input_lines)
# print('Answer ', bags_count)

import re

filename = "input.txt"

p1sum = 0
bags = {}

# Recursive function to check if a bag can be traced to "shiny gold"
def checkBags(bag):
    global p1sum
    for bagName, bagVal in bag.items():

        # If shiny gold has been reached, completely break out of function call for the given outer bag to move on
        if bagName == "shiny gold":
            p1sum += 1
            raise Exception("Found valid bag path")
        elif bags[bagName] != 0:
            checkBags(bags[bagName])
        else:
            continue


def part1():
    with open(filename, 'r') as file:
        line = file.readline().strip()
        while line:
            line = line.split()

            # The first two words of every line will always be the bag description
            keyBag = "{adj} {col}".format(adj=line[0], col=line[1])
            valBags = {}    # Stores which bags can be put into the current key bag

            # Start at index 4 because indexes 0-3 describe the initial bag, we need to parse rest of the line
            for i in range(4, len(line)):
                if line[i] == "no":
                    valBags = 0
                    break

                # If the current word is a number, it is guaranteed that the next two words are a bag description
                elif re.search("^[0-9]$", line[i]) is not None:
                    tempBagNum = int(line[i])
                    tempBagKey = "{adj} {col}".format(adj=line[i+1], col=line[i+2])
                    valBags[tempBagKey] = tempBagNum    # Add this inner bag to the list of bags that can be put in keyBag
            bags[keyBag] = valBags
            line = file.readline().strip()
    for outerBag in bags.keys():
        if bags[outerBag] != 0:

            # Checks if the current bag can be traced back to "shiny gold" bag
            # checkBags raises exception to break out of recursion if it reaches "shiny gold" at any point, so
            # it will increment the counter and move on to check the next outer bag
            try:
                checkBags(bags[outerBag])
            except:
                continue

# Part 1
part1()
print("Answer to Part 1: {}".format(p1sum))