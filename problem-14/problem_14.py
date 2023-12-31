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

def generate_contigs_from_reads(kmers):
    graph = debrujin_graph(kmers)
    degrees = graph_degrees(graph)
    contigs = []

    for v in graph.keys():
        if degrees[v] == [1, 1]:
            continue
        for u in graph[v]:
            contig = v
            w = u
            while True:
                contig += w[-1]
                w_degree = degrees[w]
                if w_degree == [1, 1]:
                    w = graph[w][0]
                else:
                    break
            contigs.append(contig)
    return sorted(contigs)

def graph_degrees(graph):
    degrees = {}
    for i in graph.keys():
        neighbors = graph[i]
        out_degree = len(neighbors)

        if i in degrees:
            degrees[i][1] = out_degree
        else:
            degrees[i] = [0, out_degree]

        for j in neighbors:
            if j in degrees:
                degrees[j][0] += 1
            else:
                degrees[j] = [1, 0]

    return degrees

if __name__ == "__main__":
    data = "".join(open('dataset.txt')).split()
    # print(data)
    print(*generate_contigs_from_reads(data[0:]))
