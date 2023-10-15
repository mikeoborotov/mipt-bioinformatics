def string_reconstruction_from_read_pairs(patterns, d):
    return genome_path_problem(eulerian_path(debruijn_from_read_pairs(patterns)), d)

def genome_path_problem(path, d):
    text = path[0][0]
    for pair in path[1: d + 2]:
        text += pair[0][-1]

    text += path[0][1]
    for pair in path[1:]:
        text += pair[1][-1]

    return text

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

# Paired prefix
def paired_prefix(pair):
    return (pair[0][:-1], pair[1][:-1])

# Paired suffix
def paired_suffix(pair):
    return (pair[0][1:], pair[1][1:])

# Calc debruijn from pairs
def debruijn_from_read_pairs(read_pairs):
    read_pairs = list(read_pairs)
    dict = {}
    for pair in read_pairs:
        pair = pair.split('|')

        suffix = paired_suffix(pair)
        prefix = paired_prefix(pair)

        if prefix in dict.keys():
            dict[prefix].append(suffix)
        else:
            dict[prefix] = [suffix]
    return dict

if __name__ == "__main__":
    data = "".join(open('dataset.txt')).split()
    #print(data)
    print(string_reconstruction_from_read_pairs(data[2:], int(data[1])))
