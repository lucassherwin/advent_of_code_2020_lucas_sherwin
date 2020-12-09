with open('input.txt', 'r') as file:
    input_lines = file.readlines()

# part 1
def find_bootloop(input):
    # instructions that have already been executed
    executed = set()

    # keep track of the value in acc
    acc = 0

    i = 0
    while i < len(input):
        print(input[i])
        
        # loop found
        if i in executed:
            print('acc = ', acc)
            # false means it still is in a loop
            return False
        # get the instruction to be executed
        inst = input[i].split()
        # seperate operation and argument
        op = inst[0]
        arg = int(inst[1])

        if op == 'acc':
            acc += arg
        elif op == 'jmp':
            executed.add(i)
            i += arg
            continue
        else:
            print('how did i get here', i)
        executed.add(i)
        i += 1
    # no boot loop found
    print('acc = ', acc)
    return acc

# finds bad instruction
def find_bad_inst(input):
    # copy the input to test
    copy = input.copy()

    # loop over the input 
    for i in range(len(copy)):
        # check if the instruction is nop
        if 'nop' in copy[i]:
            # if so swap nop and jmp
            copy[i] = copy[i].replace('nop', 'jmp')
            # test it
            test = find_bootloop(copy)
            # if find_bootloop returns true
            if test is not False:
                # find_bootloop() will return acc if it is not found
                print('acc = ', test)
                # break out of the loop
                break
            # find_bootloop returns false
            else:
                # bootloop was found
                continue
        elif 'jmp' in copy[i]:
            # replace jmp with nop
            copy[i] = copy[i].replace('jmp', 'nop')
            # test
            test = find_bootloop(copy)
            # print('elif jmp', 'test', test, 'i', i)
            # if its not false
            if test is not False:
                # no loop found
                print('acc = ', test)
                break
            # reset the input and continue
        copy = input.copy()


find_bad_inst(input_lines)
# incorrect: 1744 (too high)

# find_bootloop(input_lines)