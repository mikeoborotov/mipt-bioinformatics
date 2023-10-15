def string_spelled_by_gapped_patterns(path, k, d):
    first_patterns = [n for n, m in path]
    second_patterns = [m for n, m in path]
    prefix_string = string_spelled_by_patterns(first_patterns, k)
    suffix_string = string_spelled_by_patterns(second_patterns, k)
    for i in range((k + d + 1), len(prefix_string)):
        if prefix_string[i] != suffix_string[i - k - d]:
            return "There is no string spelled by the gapped patterns"
    return prefix_string + suffix_string[-k - d:]


def string_spelled_by_patterns(patterns, k):
    str = patterns[0]
    for i in range(1, len(patterns)):
        str += patterns[i][-1]
    return str


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

# Return string suffix
def suffix(string):
    return string[1:]

# Return string prefix
def prefix(string):
    return string[0:-1]


if __name__ == "__main__":
    data = "".join(open('dataset.txt')).split()
    # print(data)
    print(string_spelled_by_gapped_patterns(eulerian_path(debruijn_from_read_pairs(data[2:])), int(data[0]),
                                            int(data[1])))