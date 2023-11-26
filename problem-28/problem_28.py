from collections import defaultdict
import re

# 2-break distance problem
def two_break_distance_problem(P, Q):
    # initialize graph
    graph = defaultdict(list)

    # run through genomes
    for j in P + Q:
        length = len(j)
        for i in range(length):
            graph[j[i]].append(-1 * j[(i + 1) % length])
            graph[-1 * j[(i + 1) % length]].append(j[i])

    # set up counting
    count = 0
    remaining = set(graph.keys())

    # run through remaining
    while remaining:
        count += 1
        queue = {remaining.pop()} # pop one
        # and run through
        while queue:
            current = queue.pop()
            new = {i for i in graph[current] if i in remaining}
            queue |= new
            remaining -= new
    result = sum(map(len, P)) - count # calc the result

    return result


if __name__ == '__main__':
    # read and prepare dataset
    with open('dataset.txt') as file:
        P, Q = [line.strip().lstrip('(').rstrip(')').split(')(') for line in file]
        P = [list(map(int, i.split())) for i in P] # 1st genome
        Q = [list(map(int, i.split())) for i in Q] # 2nd genome

    # result
    print(two_break_distance_problem(P, Q))