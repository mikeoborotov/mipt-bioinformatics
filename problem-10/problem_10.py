# calculate hamming distance function
def hamming_dist(pattern_1, pattern_2):
    result = 0
    for i in range(len(pattern_1)):
        if pattern_1[i] != pattern_2[i]:
            result += 1
    return result

# compute the distance between a pattern and dna strings
def distance_between_pattern_and_strings(pattern, dna):
    # initialize variables
    k = len(pattern)
    total_dist = 0
    
    # iterate through each string "text" in dna
    for text in dna:
        min_hamming_dist = float('inf') # initialize dist to inf
        
        # for each kmer pattern in "text"
        for i in range(len(text) - k + 1):
            kmer = text[i:i + k]
            current_dist = hamming_dist(pattern, kmer)
            
            # if closer then update min hamming dist
            if current_dist < min_hamming_dist:
                min_hamming_dist = current_dist
        
        total_dist += min_hamming_dist
    
    return total_dist

if __name__ == "__main__":
	# initialize the variables
    pattern = ""
    dna = []

    # read the dataset from file
    with open("dataset.txt", "r") as file:
        lines = file.readlines()
        pattern = lines[0].strip()
        dna = lines[1].split()

    # calculate the result
    result = distance_between_pattern_and_strings(pattern, dna)
    print(result)
