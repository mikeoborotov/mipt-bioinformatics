# Find a longest common subsequence of multiple strings.
def multiple_alignment_score(strings):
    n = len(strings[0])
    m = len(strings[1])
    p = len(strings[2])

    # Initialize a 3D array to store scores for the alignments
    dp = [[[0] * (p + 1) for _ in range(m + 1)] for _ in range(n + 1)]

    # Fill in the dp array using dynamic programming
    for i in range(1, n + 1):
        for j in range(1, m + 1):
            for k in range(1, p + 1):
                score = 1 if strings[0][i - 1] == strings[1][j - 1] == strings[2][k - 1] else 0
                dp[i][j][k] = max(dp[i - 1][j][k], dp[i][j - 1][k], dp[i][j][k - 1],
                                  dp[i - 1][j - 1][k], dp[i - 1][j][k - 1], dp[i][j - 1][k - 1],
                                  dp[i - 1][j - 1][k - 1] + score)

    # The result is the maximum score
    max_score = dp[n][m][p]

    # Backtrack to find the actual alignment
    alignment = reconstruct_alignment(strings, dp, n, m, p)

    return max_score, alignment

# reconstruct alignment func
def reconstruct_alignment(strings, dp, i, j, k):
    alignment = [""] * 3

    while i > 0 and j > 0 and k > 0:
        if strings[0][i - 1] == strings[1][j - 1] == strings[2][k - 1]:
            alignment[0] = strings[0][i - 1] + alignment[0]
            alignment[1] = strings[1][j - 1] + alignment[1]
            alignment[2] = strings[2][k - 1] + alignment[2]
            i -= 1
            j -= 1
            k -= 1
        elif dp[i - 1][j][k] >= dp[i][j - 1][k] and dp[i - 1][j][k] >= dp[i][j][k - 1]:
            alignment[0] = strings[0][i - 1] + alignment[0]
            alignment[1] = "-" + alignment[1]
            alignment[2] = "-" + alignment[2]
            i -= 1
        elif dp[i][j - 1][k] >= dp[i - 1][j][k] and dp[i][j - 1][k] >= dp[i][j][k - 1]:
            alignment[0] = "-" + alignment[0]
            alignment[1] = strings[1][j - 1] + alignment[1]
            alignment[2] = "-" + alignment[2]
            j -= 1
        else:
            alignment[0] = "-" + alignment[0]
            alignment[1] = "-" + alignment[1]
            alignment[2] = strings[2][k - 1] + alignment[2]
            k -= 1

    while i > 0:
        alignment[0] = strings[0][i - 1] + alignment[0]
        alignment[1] = "-" + alignment[1]
        alignment[2] = "-" + alignment[2]
        i -= 1

    while j > 0:
        alignment[0] = "-" + alignment[0]
        alignment[1] = strings[1][j - 1] + alignment[1]
        alignment[2] = "-" + alignment[2]
        j -= 1

    while k > 0:
        alignment[0] = "-" + alignment[0]
        alignment[1] = "-" + alignment[1]
        alignment[2] = strings[2][k - 1] + alignment[2]
        k -= 1

    return alignment


if __name__ == '__main__':
    # read the dataset from file
    strings = []
    with open("dataset.txt", "r") as file:
        lines = file.readlines()
        for i in range(0, 3):
            strings.append(lines[i].strip())
    
    # calculate
    max_score, alignment = multiple_alignment_score(strings)

    # result
    print(max_score)
    for line in alignment:
        print(line)