# calculate hamming distance function
def hamming_dist(pattern_1, pattern_2):
    result = 0
    for i in range(len(pattern_1)):
        if pattern_1[i] != pattern_2[i]:
            result += 1
    return result

def approximate_pattern_matching(pattern, genome, d):
    positions = [] # initialize starting positions
    
    # iterate through the genome
    for i in range(len(genome) - len(pattern) + 1):
        # calculate substring
        substring = genome[i:i + len(pattern)]

        # check hamming distance
        if hamming_dist(pattern, substring) <= d:
            positions.append(i) # add position to result if less than d
    
    return positions

if __name__ == "__main__":
	# initialize the variables
    pattern = genome = ""
    d = 0

    # read the dataset from file
    with open("problem_03_dataset.txt", "r") as file:
        lines = file.readlines()
        pattern = lines[0].strip()
        genome = lines[1].strip()
        d = int(lines[2].strip())

    # calculate the result
    result = approximate_pattern_matching(pattern, genome, d)
    for i in result:
        print(i, end=" ")
    print()
