# number of breakpoints problem
def number_of_breakpoints(permutation):
    num = 0

    # run through permutation
    for i in range(len(permutation) - 1):
        if permutation[i + 1] - permutation[i] == 1:
            num += 1

    if permutation[0] == 1:
        num += 1
    if permutation[-1] == len(permutation):
        num += 1

    return len(permutation) + 1 - num

if __name__ == '__main__':
    # read and prepare the dataset
    with open('dataset.txt') as file:
        permutation = file.readline().strip()
    permutation = permutation[1:-1].split()
    permutation = [int(i) for i in permutation]

    # result
    print(number_of_breakpoints(permutation))