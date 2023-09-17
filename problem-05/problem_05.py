# calculate hamming distance function
def hamming_dist(pattern_1, pattern_2):
    result = 0
    for i in range(len(pattern_1)):
        if pattern_1[i] != pattern_2[i]:
            result += 1
    return result


# generate reverse complement for a pattern
def generate_reverse_complement(pattern):
    complement = {'A': 'T', 'T': 'A', 'C': 'G', 'G': 'C'}
    return ''.join(complement[base] for base in reversed(pattern))


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


def find_frequent_words_with_mismatches_and_reverse_complements(genome, k, d):
    pattern_counter = {} # dictionary for counting patterns
    
    # sliding window approach
    for i in range(len(genome) - k + 1):
        pattern = genome[i:i + k] # generate pattern
        similar_patterns = generate_similar_patterns(pattern, d) # generate similar patterns
        
        # count through all similar patterns
        for similar_pattern in similar_patterns:
            # count through similar patterns
            if similar_pattern in pattern_counter:
                pattern_counter[similar_pattern] += 1
            else:
                pattern_counter[similar_pattern] = 1
            
            # count through similar pattern reverse complements
            similar_pattern_reverse_complement = generate_reverse_complement(similar_pattern)
            if similar_pattern_reverse_complement in pattern_counter:
                pattern_counter[similar_pattern_reverse_complement] += 1
            else:
                pattern_counter[similar_pattern_reverse_complement] = 1
    
    # calculate most frequent patterns
    result = [pattern for pattern, count in pattern_counter.items() if count == max(pattern_counter.values())]
    
    return result


if __name__ == "__main__":
    # initialize the variables
    genome = ""

    # read the dataset from file
    with open("problem_05_dataset.txt", "r") as file:
        lines = file.readlines()
        genome = lines[0].strip()
        k, d = map(int, lines[1].split())

    # calculate the result
    result = find_frequent_words_with_mismatches_and_reverse_complements(genome, k, d)
    for i in result:
        print(i, end=" ")
    print()
