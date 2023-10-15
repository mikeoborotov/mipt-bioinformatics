import itertools

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

# Solve eulerian cycle problem
def eulerian_cycle(dict):
    stack = []
    random_vertex = sorted(dict.keys())[0]
    stack.append(random_vertex)
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

# Calc binary strings
def binary_strings(k):
    universe = ["0", "1"]
    kmers = ["".join(el) for el in itertools.product(universe, repeat=k)]
    return sorted(kmers)

def k_universal_string(k):
    cycle = eulerian_cycle(debrujin_graph(binary_strings(k)))
    cycle = cycle[:-(k-1)]
    genome = cycle[0][:-1]
    for i in cycle:
        genome += i[-1]
    return genome

if __name__ == "__main__":
    dataset = 9
    print(k_universal_string(dataset))
