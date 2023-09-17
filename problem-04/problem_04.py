# calculate hamming distance function
def hamming_dist(pattern_1, pattern_2):
    result = 0
    for i in range(len(pattern_1)):
        if pattern_1[i] != pattern_2[i]:
            result += 1
    return result

# generate all similar patterns (patterns with d mismatches)
def generate_similar_patterns(pattern, d):
    if d == 0:
        return [pattern]
    if len(pattern) == 1:
        # if len=1 then only these options (all possible nucleotides)
        return ['A', 'C', 'G', 'T']
    
    similar_patterns = [] # initialize similar patterns array
    similar_subpatterns = generate_similar_patterns(pattern[1:], d) # recursive call for a subpattern
    
    # run through all similar subpatterns
    for similar_subpattern in similar_subpatterns:
        if hamming_dist(pattern[1:], similar_subpattern) < d:
            # if within hamming distance then add all subpatterns
            for i in ['A', 'C', 'G', 'T']:
                similar_patterns.append(i + similar_subpattern)
        else:
            similar_patterns.append(pattern[0] + similar_subpattern)
    
    return similar_patterns

def find_frequent_words_with_mismatches(genome, k, d):
    pattern_counter = {} # dictionary for counting patterns
    result = [] # initialize empty array for most frequent patterns
    
    # sliding window approach
    for i in range(len(genome) - k + 1):
        pattern = genome[i:i + k] # generate pattern
        similar_patterns = generate_similar_patterns(pattern, d) # generate similar patterns
        
        # count through all similar patterns
        for similar_pattern in similar_patterns:
            if similar_pattern in pattern_counter:
                pattern_counter[similar_pattern] += 1
            else:
                pattern_counter[similar_pattern] = 1
    
    # calculate most frequent patterns
    for pattern, count in pattern_counter.items():
        if count == max(pattern_counter.values()):
            result.append(pattern)
    
    return result

if __name__ == "__main__":
	# initialize the variables
    genome = ""

    # read the dataset from file
    with open("problem_04_dataset.txt", "r") as file:
        lines = file.readlines()
        genome = lines[0].strip()
        k, d = map(int, lines[1].split())

    # calculate the result
    result = find_frequent_words_with_mismatches(genome, k, d)
    for i in result:
        print(i, end=" ")
    print()
