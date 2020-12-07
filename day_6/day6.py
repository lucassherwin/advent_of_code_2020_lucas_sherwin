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
            answers |= set(i.strip().split())
        # if the line is blank
        else:
            # add the length to the total number of questions
            total += len(answers)
            # clear the set
            answers.clear()
    print(total)
    return total


# incorrect: 1608



count_yes(input_lines)