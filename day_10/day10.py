# example.txt
# larger_example.txt
# input.txt

with open('input.txt', 'r') as file:
    input_lines = [int(line.strip()) for line in file]

def test_adapters(input):
    input.append(0)
    input.sort()

    # keep track of the numbers with either a 1 jolt diff or a 3 jolt diff
    one_diff = 0
    three_diff = 1

    for i in range(len(input)-1):
        if input[i] + 3 == input[i+1]:
            three_diff += 1
        elif input[i] + 2 == input[i+1]:
            continue
        elif input[i] + 1 == input[i+1]:
            one_diff += 1
    ans = one_diff * three_diff
    # max = max(input)
    print(ans)
    return ans

test_adapters(input_lines)

# incorrect: 1536 (too low)