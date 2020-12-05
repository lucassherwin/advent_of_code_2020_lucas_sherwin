# with open('input.txt', 'r') as file:
#     input_lines = file.readlines()


# def count_valid_passports(input):
#     # passport object to check if each one is valid
#     passport = {
#         'byr': False,
#         'iyr': False,
#         'eyr': False,
#         'hgt': False,
#         'hcl': False,
#         'ecl': False,
#         'pid': False
#     }

#     required = ["byr", "iyr", "eyr", "hgt", "hcl", "ecl", "pid"]

#     count = 0

#     for i in input:
#         i = i.strip()

#         # check if the line is blank indicating that the passport is finished
#         if len(i) == 0:
#             # create a list of the current keys
#             currentKeys = list(passport.keys())
#             # check if the length of the currentKeys is less than the length of the required keys
#             if len(i) < len(required):
#                 pass
#             else:
#                 validPassport = True
#                 for key in currentKeys:
#                     # check if the key is 'cid' which is not required
#                     if key == 'cid':
#                         continue
#                     # check if the key is false
#                     elif passport[key] == False:
#                         # if one key is false the entire passport is invalid
#                         validPassport = False
#                         break
#                 # if the passport is valid increase the count
#                 if validPassport:
#                     count += 1
#             # reset the passport
#             passport = {
#                 'byr': False,
#                 'iyr': False,
#                 'eyr': False,
#                 'hgt': False,
#                 'hcl': False,
#                 'ecl': False,
#                 'pid': False
#             }
#         # still in a current passport
#         else:
#             # split each item
#             items = i.split()
#             for elem in items:
#                 # split each part at the ':'
#                 parts = elem.split(':')
#                 field = parts[0]
#                 # skip 'cid' as it is not required
#                 if field == 'cid':
#                     continue
#                 else:
#                     # set the found field to true
#                     passport[field] = True
#                 print(passport, count)
#     print(count)
#     return count

# count_valid_passports(input_lines)

import re

p2incorrect = [138, 102]

filename = "input.txt"

with open(filename, 'r') as file:
    inp = file.readlines()

# Regex expressions for each field for Part 2
byr = "(^19[2-9][0-9]$)|(^200[0-2]$)"
iyr = "^20(1[0-9]|20)$"
eyr = "^20(2[0-9]|30)$"
hgt = "^1([5-8][0-9]|9[0-3])cm|(59|(6[0-9]|7[0-6]))in$"
hcl = "^#[0-9a-f]{6}$"
ecl = "^(amb|blu|brn|gry|grn|hzl|oth)$"
pid = "^[0-9]{9}$"
regexs = {"byr": byr, "iyr": iyr, "eyr": eyr, "hgt": hgt, "hcl": hcl, "ecl": ecl, "pid": pid}


def countValid(data, verifyFields):
    count = 0
    fieldStatus = {"byr": False, "iyr": False, "eyr": False, "hgt": False, "hcl": False, "ecl": False,
                   "pid": False}  # Initialize passport to no valid fields
    required = ["byr", "iyr", "eyr", "hgt", "hcl", "ecl", "pid"]

    for line in data:
        line = line.strip()

        # Found a blank line, meaning previous passport is finished loading and ready to check
        if len(line) == 0:
            currentKeys = list(fieldStatus.keys())
            if len(currentKeys) < len(required):
                pass
            else:
                validPassport = True
                for key in currentKeys:
                    if key == "cid":
                        continue
                    elif fieldStatus[key] == False:
                        validPassport = False
                        break

                if validPassport:
                    count += 1

            # Clear previous passport data to prepare for the next one
            fieldStatus = {"byr": False, "iyr": False, "eyr": False, "hgt": False, "hcl": False, "ecl": False,
                           "pid": False}
        else:
            items = line.split()
            for elem in items:
                parts = elem.split(':')
                field = parts[0]
                if field == "cid":
                    continue
                if verifyFields:
                    if re.search(regexs[field], parts[1]) is not None:
                        fieldStatus[field] = True
                else:
                    fieldStatus[field] = True
                # print(fieldStatus)
    return count


print("Answer for Part 1: {}".format(countValid(inp, False)))
print("Answer for Part 2: {}".format(countValid(inp, True)))