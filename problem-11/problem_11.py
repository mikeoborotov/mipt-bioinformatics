# Return string suffix
def suffix(string):
    return string[1:]

# Return string prefix
def prefix(string):
    return string[0:-1]

# Calc suffix composition
def suffix_compose(k, text, uniq=False):
    kmers = []
    for i in range(len(text)+1-k):
        kmers.append(text[i:i+k-1])
    if uniq:
        return sorted(list(kmers))
    else:
        return sorted(kmers)

# Calc debrujin graph from k-mers
def debrujin_graph(patterns):
    kmers = []
    for pattern in patterns:
        kmers = kmers + suffix_compose(len(pattern), pattern, uniq=True)
    kmers = set(kmers)
    dict = {}
    for kmer1 in kmers:
        dict[kmer1] = []
    for kmer in patterns:
        dict[prefix(kmer)].append(suffix(kmer))
    return dict

def balance_count(input):
    result = dict.fromkeys(input.keys(), 0)
    # Look for nodes balancing
    for node in input.keys():
        for out in input[node]:
            result[node] -= 1
            try:
                result[out] += 1
            except:
                result[out] = 1
    return result

# Solve eulerian path problem
def eulerian_path(dict):
    stack=[]
    balanced_count = balance_count(dict)
    stack.append([k for k, v in balanced_count.items() if v==-1][0])
    path = []
    while stack != []:
        u_v = stack[-1]
        try:
            w = dict[u_v][0]
            stack.append(w)
            dict[u_v].remove(w)
        except:
            path.append(stack.pop())
    return path[::-1]

# Solve genome path problem
def genome_path(kmers, apppend_last=True):
    genome = ''
    kmer_length = len(kmers[0])
    for kmer in kmers:
        genome += kmer[0]
    if apppend_last:
        genome += kmer[1:]
    return genome

# String reconstruction problem function
def reconstruct_string(patterns):
    return genome_path(eulerian_path(debrujin_graph(patterns)))

if __name__ == "__main__":
    # initialize the variables
    patterns = []
    k = 0

    # read the dataset from file
    with open("dataset.txt", "r") as file:
        lines = file.readlines()
        k = int(lines[0].strip())
        lines = lines[1:]
        for line in lines:
            patterns.append(line.strip())

    # calculate the result
    result = reconstruct_string(patterns)
    print(result)
