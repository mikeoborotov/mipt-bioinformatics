import numpy as np

# calculate colored edges
def colored_edges(genome):
    # init 
    result = []

    # run through genome
    for i in genome:
        s = chromosome_to_cycle(i)
        for j in range(len(s) // 2):
            head = 1 + 2 * j # calculate head
            tail = (2 + 2 * j) % len(s) # calculate tail
            e = (s[head], s[tail])
            result.append(e)

    return result

# two break sorting problem
def two_break_sorting(P, Q):
    # init
    colored = colored_edges(Q)
    path = [P]

    # sort
    while two_break_distance(P, Q) > 0:
        cycles = colored_edges_cycles(colored_edges(P), colored)
        for i in cycles:
            if len(i) >= 4:
                P = two_break_on_genome(P, i[0], i[1], i[3], i[2])
                path.append(P)
                break

    return path

# two break on genome
def two_break_on_genome(genome, i, j, k, l):
    graph = colored_edges(genome)
    graph = two_break_on_genome_graph(graph, i, j, k, l)
    genome = graph_to_genome(graph)
    return genome

# two break on genome graph
def two_break_on_genome_graph(graph, i, j, k, l):
    rem = ((i, j), (j, i), (k, l), (l, k))
    bg = [t for t in graph if t not in rem]
    bg.append((i, k))
    bg.append((j, l))
    return bg

# calculate dist
def two_break_distance(P, Q):
    blue = colored_edges(P)
    red = colored_edges(Q)

    size = len(blue) + len(red)

    length = colored_edges_cycles(blue, red)

    return size // 2 - len(length)


def permutation_list_to_string(p):
    ps = []
    for i in p:
        if i > 0:
            ps.append('+' + str(i))
        elif i == 0:
            ps.append('0')
        elif i < 0:
            ps.append(str(i))
    return '(' + ' '.join(ps) + ')'


def permutation_string_to_list(str_p):
    p = list(map(int, str_p.strip()[1:-1].split(' ')))
    return p


def format_sequence(s):
    fs = []
    for i in s:
        str_p = permutation_list_to_string(i)
        fs.append(str_p)
    return fs

# chromosome to cyc func
def chromosome_to_cycle(p):
    nodes = []
    for i in p:
        if i > 0:
            nodes.append(2 * i - 1)
            nodes.append(2 * i)
        else:
            nodes.append(-2 * i)
            nodes.append(-2 * i - 1)
    return nodes


# cyc to chromosome func
def cycle_to_chromosome(nodes):
    p = []
    for j in range(0, len(nodes) // 2):
        if nodes[2 * j] < nodes[2 * j + 1]:
            s = j + 1
        else:
            s = -(j + 1)
        p.append(s)
    return p


def genome_str_to_list(genome):
    lp = []
    for p in genome.split('(')[1:]:
        p = permutation_string_to_list('(' + p)
        lp.append(p)
    return lp

# convert graph to genome func
def graph_to_genome(g):

    genome = []
    visited = []

    adj = np.zeros(len(g) * 2, dtype=np.int)

    for t in g:
        adj[t[0] - 1] = t[1] - 1
        adj[t[1] - 1] = t[0] - 1

    for t in g:
        orig = t[0]

        if orig in visited:
            continue

        visited.append(orig) # visit

        if (orig % 2 == 0):
            closing = orig - 1
        else:
            closing = orig + 1

        p = []
        i = 0

        while (True):

            if (orig % 2 == 0):
                p.append(orig // 2)
            else:
                p.append(-(orig + 1) // 2)
            dest = adj[orig - 1] + 1
            i = i + 1

            if (i > 100):

                return
            visited.append(dest)

            if (dest == closing):
                genome.append(p)
                break
            if (dest % 2 == 0):
                orig = dest - 1
            else:
                orig = dest + 1

            assert orig > 0

            visited.append(orig)

    return genome


# colored edges cycles for blue and red
def colored_edges_cycles(blue, red):
    # init
    cycles = []
    size = len(blue) + len(red)

    adj = np.zeros(shape=(size, 2), dtype=np.int)
    visiteded = np.zeros(shape=size, dtype=np.bool)

    # run through blue and red
    for e in blue:
        adj[e[0] - 1, 0] = e[1] - 1
        adj[e[1] - 1, 0] = e[0] - 1
    for e in red:
        adj[e[0] - 1, 1] = e[1] - 1
        adj[e[1] - 1, 1] = e[0] - 1

    # run through nodes
    for node in range(size):
        if not visiteded[node]:

            visiteded[node] = True # visit
            head = node # upd head

            cycle = [head + 1]
            color = 0

            while True:
                node = adj[node, color]

                if node == head:
                    cycles.append(cycle)
                    break

                cycle.append(node + 1)
                visiteded[node] = True
                color = (color + 1) % 2

    return cycles


if __name__ == '__main__':
    # read and prepare dataset
    with open('dataset.txt') as file:
        P = [list(map(int, file.readline().strip()[1:-1].split(' ')))]
        Q = [list(map(int, file.readline().strip()[1:-1].split(' ')))]
    path = two_break_sorting(P, Q) # sort
    
    # print result
    for i in path:
        print(''.join(format_sequence(i)))