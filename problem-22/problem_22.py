# Length of a Longest Path in the Manhattan Tourist Problem
def manhatan_tourist_problem(n, m, down_matrix, right_matrix):
    # initialize a matrix to store the lengths of the longest paths
    matrix = [[0] * (m + 1) for _ in range(n + 1)]

    # fill in the matrix (dynamic programming)
    for i in range(1, n + 1):
        matrix[i][0] = matrix[i - 1][0] + down_matrix[i - 1][0]
    for j in range(1, m + 1):
        matrix[0][j] = matrix[0][j - 1] + right_matrix[0][j - 1]
    for i in range(1, n + 1):
        for j in range(1, m + 1):
            matrix[i][j] = max(matrix[i - 1][j] + down_matrix[i - 1][j], matrix[i][j - 1] + right_matrix[i][j - 1])

    return matrix[n][m]


if __name__ == "__main__":
    with open('dataset.txt') as file:
        line = file.readline().strip().split()

        # read dimentions
        n = int(line[0])
        m = int(line[1])

        # read down matrix
        down_matrix = []
        for i in range(n):
            line = file.readline().strip().split()
            down_matrix.append([int(i) for i in line])
        file.readline()

        # read right matrix
        right_matrix = []
        for i in range(n + 1):
            line = file.readline().strip().split()
            right_matrix.append([int(i) for i in line])

    # calculate
    print(manhatan_tourist_problem(n, m, down_matrix, right_matrix))