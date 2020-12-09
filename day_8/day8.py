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

        if i in executed:
            print('acc = ', acc)
            return acc
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
    print('acc = ', acc)
    return acc

find_bootloop(input_lines)