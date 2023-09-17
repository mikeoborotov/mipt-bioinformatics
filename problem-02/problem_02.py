def find_minimum_skew(genome):
    skew = 0 # initialize skew as 0
    min_skew = 0 # initialize mininum skew as 0
    min_skew_positions = [] # a list of positions with minimum skew
    
    # iterate through the genome
    for i in range(len(genome)):
        # calculate skew
        if genome[i] == 'G':
            skew += 1
        elif genome[i] == 'C':
            skew -= 1
        
        # check for the minimum skew
        if skew < min_skew:
            min_skew = skew
            min_skew_positions = [i + 1] # if below minimum skew reset positions
        elif skew == min_skew:
            min_skew_positions.append(i + 1) # if the same as minimum skew add the position
    
    return min_skew_positions

if __name__ == "__main__":
	# initialize the variables
    genome = ""

    # read the dataset from file
    with open("problem_02_dataset.txt", "r") as file:
        lines = file.readlines()
        genome = lines[0].strip()

    # calculate the result
    result = find_minimum_skew(genome)
    for i in result:
        print(i, end=" ")
    print()
