import copy

# greedy sorting algorithm
def greedy_sorting(permutation):
    # initial
    approx_reversal_dist = 0
    permutations = [] # empty

    # run through permutation
    for i in range(1, len(permutation) + 1):
        # if not = i or -i
        if permutation[i - 1] != i and permutation[i - 1] != -i:
            index = 0

            # check if in permutation
            if i in permutation:
                index = permutation.index(i)
            elif -i in permutation:
                index = permutation.index(-i)

            tem = permutation[i - 1:index + 1]
            tem = [-k for k in tem]

            permutation[i - 1:index + 1] = tem[::-1]
            permutations.append(copy.copy(permutation)) # add permutation

            approx_reversal_dist += 1 # increase distance

        # if opposite
        if permutation[i - 1] == -i:
            permutation[i - 1] = i
            permutations.append(copy.copy(permutation))

            approx_reversal_dist += 1 # increase distance

    return approx_reversal_dist, permutations


if __name__ == '__main__':
    # read and prepare the dataset
    with open('dataset.txt') as f:
        permutation = f.readline().strip()
    permutation = permutation[1:-1].split()
    permutation = [int(i) for i in permutation]

    # result
    approx_reversal_dist, permutations = greedy_sorting(permutation)

    for i in permutations:
        # print like an example
        str_p = ['+' + str(j) if j > 0 else str(j) for j in i]
        print('(%s)' % ' '.join(str_p))