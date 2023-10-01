def sample(sample_input):
    result = set() # initialize result patterns as an empty set
    
    return result

if __name__ == "__main__":
	# initialize the variables
    genome = ""

    # read the dataset from file
    with open("problem_02_dataset.txt", "r") as file:
        lines = file.readlines()
        genome = lines[0].strip()

    # calculate the result
    result = sample(genome, k, d)
    for i in result:
        print(i, end=" ")
    print()
