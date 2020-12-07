with open('input.txt', 'r') as file:
    input_lines = file.readlines()

# counting the number of questions answered "yes" to
def count_yes(input):
    # total to be returned at the end
    total = 0
    
    # set to keep track of the questions answered "yes" to 
    # using a set to get rid of duplicates
    answers = set()

    for i in input:
        # if there are characters in the line add them to the set
        if i.strip() != '':
            answers |= set(list(i.strip()))
        # if the line is blank
        else:
            # add the length to the total number of questions
            total += len(answers)
            # clear the set
            answers.clear()
    print(total)
    return total

def count_yes_part2(input):
    # track the total number of questions that everyone answered "yes" to
    total = 0

    # set to keep track of questions everyone answered "yes" to
    answer = set({'a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z'})
    for i in input:
        if i.strip() != '':
            answer = answer.intersection(set(list(i.strip())))
        else:
            total += len(answer)
            answer = set({'a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z'})
    print(total)
    return total



# pt1 incorrect: 1608, 6668



count_yes(input_lines)

count_yes_part2(input_lines)