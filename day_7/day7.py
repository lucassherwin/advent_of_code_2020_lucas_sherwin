import re

with open('input.txt', 'r') as file:
    input_lines = file.readlines()

bags_count = 0

# list of all bags
bags = {}

def how_many_bags(input):
    # bags = {}
    for i in input:
        rule = i.strip().split('contain')
        # print(i)
        bag_key = rule[0].strip().replace('bags', '') 
        # store the bags that can be put into the current bag key
        val_bags = {}
        # print(rule[1])

        if 'no' in rule[1]:
            val_bags = 0
        else:
            # temp = [item.strip() for item in rule[1].split(',')]
            # print('temp', temp)
            # for t in temp:
            for t in [item.strip() for item in rule[1].split(',')]:
                temp_bag_num = t[0]
                temp_bag_key = re.sub(r'[0-9]+', '', t).replace('bags', '').replace('.', '').strip()
                # print(temp_bag_num, temp_bag_key)
                val_bags[temp_bag_key] = temp_bag_num
        bags[bag_key] = val_bags
    
    for outer_bag in bags.keys():
        if bags[outer_bag] != 0:
            try:
                check_bag(bags[outer_bag])
            except:
                continue

# recursive function
def check_bag(bag):
    global bags_count

    for bag_name, bag_val in bag.items():
        # if we reach a shiny gold bag break out of function and move to next outer_bag
        if bag_name == 'shiny gold':
            bags_count += 1
            raise Exception('Found path')
        elif bags[bag_name] != 0:
            check_bag(bags[bag_name])
        else:
            continue








how_many_bags(input_lines)
print('Answer ', bags_count)