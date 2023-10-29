# expand the peptides
def expand(peptides):
    # new peptides array
    new_peptides = []

    # run through all peptides
    for peptide in peptides:
        for key in amino_acid_weight_table:
            # add new
            new_peptides.append(peptide + key)

    return new_peptides

# peptide mass
def get_peptide_mass(peptide):
    mass = 0

    for i in range(len(peptide)):
        mass += amino_acid_weight_table[peptide[i]]

    return mass


# get peptide linear spectrum
def linear_spectrum(peptide):
    prefix_mass = [0 for i in range(len(peptide) + 1)]

    # run through the peptide
    for i in range(len(peptide)):
        # calc prefix mass
        prefix_mass[i + 1] = prefix_mass[i] + amino_acid_weight_table[peptide[i]]

    result_spectrum = []

    # run through the peptide
    for i in range(len(peptide)):
        for j in range(i + 1, len(peptide) + 1):
            # spectrum
            result_spectrum.append(prefix_mass[j] - prefix_mass[i])

    result_spectrum.append(0) # add zero to spectrum
    result_spectrum = sorted(result_spectrum)

    return result_spectrum


# get parent peptide mass
def get_parent_mass(spectrum):
    return spectrum[-1]


# linear scoring func
def linear_score(peptide, spectrum):
    score = 0

    # spectrums
    peptide_spectrum = linear_spectrum(peptide)
    local_spectrum = spectrum.copy() # spectrum copy

    # scoring
    for i in peptide_spectrum:
        # check if in spectrum
        if i in local_spectrum:
            score += 1 # score one
            local_spectrum.remove(i)

    return score


# trim the leaderboard
def trim(leaderboard, spectrum, N):
    # init score array 
    scores = []

    if len(leaderboard) < N:
        result = leaderboard # copy leaderboard to result
    else:
        # else trim
        for peptide in leaderboard:
            scores.append(linear_score(peptide, spectrum))

        # sort scores
        scores.sort(reverse=True)
        score_min = scores[N - 1]

        # peptides above min score
        valid_peptide = []

        # only leave valid ones
        for i, peptide in enumerate(leaderboard):
            if linear_score(peptide, spectrum) >= score_min:
                valid_peptide.append(i)

        result = []

        # leave only valid from leaderboard
        for k in valid_peptide:
            result.append(leaderboard[k])

    return result


# leaderboard cyclopeptide sequencing func
def leaderboard_cyclopeptide_sequencing(spectrum, n):
    # init leaderboard
    leaderboard = ['']
    leader_peptide = ''
    leader_peptide_score = 0

    # run through the leaderboard
    while leaderboard:
        # expand
        leaderboard = expand(leaderboard)
        loop = list(leaderboard)

        # run through peptides
        for peptide in loop:
            # masses (weight)
            mass = get_peptide_mass(peptide)
            parent_mass = get_parent_mass(spectrum)

            # scoring
            if mass == parent_mass:
                score = linear_score(peptide, spectrum)
                if score > leader_peptide_score:
                    leader_peptide = peptide
                    leader_peptide_score = score
            elif mass > parent_mass:
                leaderboard.remove(peptide)

        # trim leaderboard
        leaderboard = trim(leaderboard, spectrum, n)

    return leader_peptide


if __name__ == "__main__":
    # amino acid weight table (amino acid : weight)
    amino_acid_weight_table = {'G': 57,  'A': 71,  'S': 87,  'P': 97,  'V': 99,
                               'T': 101, 'C': 103, 'I': 113, 'N': 114, 'D': 115,
                               'K': 128, 'E': 129, 'M': 131, 'H': 137, 'F': 147,
                               'R': 156, 'Y': 163, 'W': 186}

    # read dataset
    with open('dataset.txt') as file:
        n = int(file.readline())
        spectrum = list(map(int, file.readline().split()))

    # leaders
    leader_peptide = leaderboard_cyclopeptide_sequencing(spectrum, n)
    leader_peptide_mass = []

    # masses
    for i in leader_peptide:
        leader_peptide_mass.append(amino_acid_weight_table[i])

    result = '-'.join([str(i) for i in leader_peptide_mass])
    print(result)
