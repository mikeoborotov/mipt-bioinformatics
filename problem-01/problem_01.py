def find_patterns_forming_clumps(genome, k, L, t):
    result = set() # initialize result patterns as an empty set

    # iterate through the genome using all possible sliding windows of lenght L
    for i in range(len(genome) - L + 1):
        window = genome[i:i + L] # sliding window of length L
        pattern_counter = {} # initialize pattern counter as an empty dictionary
        
        # iterate through possible patterns inside a window 
        for j in range(len(window) - k + 1):
            pattern = window[j:j + k]
            # count how many times the pattern appears inside a window
            if pattern in pattern_counter:
                pattern_counter[pattern] += 1
            else:
                pattern_counter[pattern] = 1
        
        # add to the result only patterns which appear t or more times
        for pattern, count in pattern_counter.items():
            if count >= t:
                result.add(pattern)
    
    return list(result)

if __name__ == "__main__":
	# initialize the variables
	genome = ""
	k = L = t = 0

	# read the dataset from file
	with open("problem_01_dataset.txt", "r") as file:
		lines = file.readlines()
		genome = lines[0].strip() 
		k, L, t = map(int, lines[1].split())

	# calculate the result
	result = find_patterns_forming_clumps(genome, k, L, t)
	for i in result:
		print(i, end=" ")
	print()
