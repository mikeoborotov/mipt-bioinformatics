import random

# find the profile-most probable k-mer in a given string
def profile_most_probable_kmer(genome, k, profile):
    # initialize variables
    max_prob = -1
    most_probable = ""
    
    # iterate through the genome
    for i in range(len(genome) - k + 1):
        kmer = genome[i:i + k] # select a kmer
        probability = 1.0
        
        # check all variations
        for j in range(k):
            if kmer[j] == 'A':
                probability *= profile[0][j]
            elif kmer[j] == 'C':
                probability *= profile[1][j]
            elif kmer[j] == 'G':
                probability *= profile[2][j]
            elif kmer[j] == 'T':
                probability *= profile[3][j]
        
        # check for most probable kmer
        if probability > max_prob:
            max_prob = probability
            most_probable = kmer
    
    return most_probable

# create a profile matrix from motifs
def create_profile(motifs):
    # initialize variables
    k = len(motifs[0])
    t = len(motifs)
    profile = [[1.0] * k for _ in range(4)] # pseudo counts of 1
    
    # iterate through all variations
    for i in range(k):
        for j in range(t):
            if motifs[j][i] == 'A':
                profile[0][i] += 1
            elif motifs[j][i] == 'C':
                profile[1][i] += 1
            elif motifs[j][i] == 'G':
                profile[2][i] += 1
            elif motifs[j][i] == 'T':
                profile[3][i] += 1
    
    # normalize
    for i in range(4):
        for j in range(k):
            profile[i][j] /= (t + 4)
    
    return profile

# scoring function for the greedy motif search (based on Hamming distance)
def score(motifs):
    # initialize variables
    k = len(motifs[0])
    t = len(motifs)
    score = 0
    
    for i in range(k):
        column = [motifs[j][i] for j in range(t)] # select column
        max_count = max(column.count('A'), column.count('C'), column.count('G'), column.count('T')) # max count in column
        score += t - max_count
    
    return score

# greedy motif search function
def greedy_motif_search(dna, k, t):
    best_motifs = [sequence[:k] for sequence in dna] # initialize best motifs with first ones in each string
    
    # iterate through dna strings
    for i in range(len(dna[0]) - k + 1):
        motif = dna[0][i:i + k]
        motifs = [motif]
        
        for j in range(1, t):
            profile = create_profile(motifs) # create a profile from motifs
            most_probable_kmer = profile_most_probable_kmer(dna[j], k, profile)
            motifs.append(most_probable_kmer)
        
        if score(motifs) < score(best_motifs):
            best_motifs = motifs
    
    return best_motifs

# randomized motif search function
def randomized_motif_search(dna, k, t):
    # randomly select kmers motifs in each string
    best_motifs = [random.choice([sequence[i:i + k] for sequence in dna]) for i in range(t)]
    
    # run many attemps
    for _ in range(1000):
        motifs = [random.choice([sequence[i:i + k] for sequence in dna]) for i in range(t)]
        
        while True:
            profile = create_profile(motifs)
            motifs = [profile_most_probable_kmer(sequence, k, profile) for sequence in dna]
            
            # if the score is not getting better then break loop
            if score(motifs) < score(best_motifs):
                best_motifs = motifs
            else:
                break
        
    return best_motifs

if __name__ == "__main__":
    # initialize the variables
    dna = []
    k = t = 0

    # read the dataset from file
    with open("dataset.txt", "r") as file:
        lines = file.readlines()
        k, t = map(int, lines[0].split())
        for i in range(0, t):
            dna.append(lines[i + 1].strip())

    # calculate the result
    result = randomized_motif_search(dna, k, t)
    for motif in result:
        print(motif)
