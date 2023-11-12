def local_alignment(sequence_1, sequence_2, score_matrix, penalty):
    # lengths 
    len1, len2 = len(sequence_1), len(sequence_2)

    # init 0 matr
    s = [[0 for i in range(len2 + 1)] for j in range(len1 + 1)]

    backtrack = [[0 for i in range(len2 + 1)] for j in range(len1 + 1)]

    max_score = -1
    max_a, max_b = 0, 0 # init to 0

    # iterate through
    for i in range(1, len1 +1):
        for j in range(1, len2+1):
            score_list = [s[i-1][j] - penalty, s[i][j-1] - penalty, s[i-1][j-1] + score_matrix[sequence_1[i-1], sequence_2[j-1]], 0]
            s[i][j] = max(score_list)
            backtrack[i][j] = score_list.index(s[i][j])
            if s[i][j] > max_score:
                max_score = s[i][j]
                max_a, max_b = i, j

    insert_indel = lambda seq, i: seq[:i] + '-' + seq[i:]

    a, b = max_a, max_b
    align1, align2 = sequence_1[:a], sequence_2[:b]

    while backtrack[a][b] != 3 and a * b != 0:
        if backtrack[a][b] == 0:
            a -= 1
            align2 = insert_indel(align2, b)
        elif backtrack[a][b] == 1:
            b -= 1
            align1 = insert_indel(align1, a)
        elif backtrack[a][b] == 2:
            a -= 1
            b -= 1

    align1 = align1[a:]
    align2 = align2[b:]

    return str(max_score), align1, align2


if __name__ == '__main__':
    # read input dataset
    with open('dataset.txt') as file_1:
        sequence_1 = file_1.readline().strip()
        sequence_2 = file_1.readline().strip()

    # read PAM250
    with open('PAM250.txt') as file_2:
        lines = [line.strip().split() for line in file_2.readlines()]
        score_matrix = {(i[0], i[1]): int(i[2]) for i in lines}

    penalty = 5

    # calculate
    result = '\n'.join(local_alignment(sequence_1, sequence_2, score_matrix, penalty))
    print(result)