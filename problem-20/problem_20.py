def get_top_m_elements(convolution_dict, m):
    convolution = [(key, val) for key, val in convolution_dict.items()]
    sorted_convolution = sorted(convolution, key=lambda entry: entry[1], reverse=True)
    trim_pos = m-1

    for trim_pos in range(m - 1, len(sorted_convolution) - 1):
        if sorted_convolution[trim_pos][1] > sorted_convolution[trim_pos + 1][1]:
            break

    return [i[0] for i in sorted_convolution[:trim_pos + 1]]


def get_spectral_convolution_dict(spectrum):
    spectrum = sorted(spectrum)
    convolution_dict = {}

    for i in range(len(spectrum) - 1):
        for j in range(i, len(spectrum)):
            mass = spectrum[j] - spectrum[i]

            if mass < 57 or mass > 200:
                continue

            if mass in convolution_dict:
                convolution_dict[mass] += 1

            else:
                convolution_dict[mass] = 1

    return convolution_dict


# expand the peptides
def expand(peptides, amino_acid_mass_list):
    # new peptides array
    new_peptides = []

    # run through all peptides
    for peptide in peptides:
        for mass in amino_acid_mass_list:
            new_peptide = list(peptide)
            new_peptide.append(mass)
            new_peptides.append(new_peptide)

    return new_peptides


# peptide mass
def get_peptide_mass(peptide):
    mass = 0

    for i in range(len(peptide)):
        mass += amino_acid_weight_table[peptide[i]]

    return mass


# get parent peptide mass
def get_parent_mass(spectrum):
    return spectrum[-1]

# scoring
def make_score(peptide, spectrum):
    linear = cyclospectrum(peptide)
    local = spectrum.copy()
    score = 0

    for i in linear:
        if i in local:
            score += 1
            local.remove(i)

    return score


def cyclospectrum(peptide):
    prefix_mass = [0]

    for i in range(len(peptide)):
        prefix_mass.append(prefix_mass[i]+peptide[i])

    theoretical_spectrum = [0]

    for i in range(len(prefix_mass) - 1):
        for j in range(i + 1, len(prefix_mass)):
            theoretical_spectrum.append(prefix_mass[j]-prefix_mass[i])
            if i > 0 and j < len(prefix_mass)-1:
                theoretical_spectrum.append(prefix_mass[-1] - (prefix_mass[j] - prefix_mass[i]))

    return sorted(theoretical_spectrum)



def linear_spectrum(peptide):
    prefix_mass = [0 for i in range(len(peptide) + 1)]

    for i in range(len(peptide)):
        prefix_mass[i + 1] = prefix_mass[i] + peptide[i]

    lin_spectrum = []

    for i in range(len(peptide)):
        for j in range(i + 1, len(peptide) + 1):
            lin_spectrum.append(prefix_mass[j] - prefix_mass[i])

    lin_spectrum.append(0)
    lin_spectrum = sorted(lin_spectrum)

    return lin_spectrum

# linear scoring
def linear_score(peptide, spectrum):

    linear = linear_spectrum(peptide)
    local = spectrum.copy()

    score = 0

    for i in linear:
        if i in local:
            score += 1
            local.remove(i)

    return score


# trim leaderboard
def trim(leaderboard, spectrum, N):
    scores = []

    if len(leaderboard) < N:
        result = leaderboard # copy leaderboard to result
    else:
        for pep in leaderboard:
            scores.append(linear_score(pep, spectrum))

        # sort scores
        scores.sort(reverse=True)

        score_min = scores[N - 1]
        valid_pep = [] # peptides above min score

        # only leave valid ones
        for i, pep in enumerate(leaderboard):
            if linear_score(pep, spectrum) >= score_min:
                valid_pep.append(i)

        result = []

        for k in valid_pep:
            result.append(leaderboard[k])

    return result


# leaderboard cyclopeptide sequencing func
def leaderboard_cyclopeptide_sequencing(spectrum, n, amino_acid_mass_list):
    # init leadearboard
    leaderboard = [[]]
    leader_peptide = ''
    leader_peptidescore = 0

    while leaderboard:
        # expand
        leaderboard = expand(leaderboard, amino_acid_mass_list)
        loop = list(leaderboard)

        # run through peptides
        for peptide in loop:
            mass = sum(peptide)
            parent_mass = get_parent_mass(spectrum)

            # scoring
            if mass == parent_mass:
                score = make_score(peptide, spectrum)
                if score > leader_peptidescore:
                    leader_peptide = peptide
                    leader_peptidescore = score
            elif mass > parent_mass:
                leaderboard.remove(peptide)

        # trim leaderboard
        leaderboard = trim(leaderboard, spectrum, n)

    return leader_peptide


# convolution
def convolution_cyclopeptide_sequencing(m, n, spectrum):
    spectrum = sorted(spectrum)
    convolution_dict = get_spectral_convolution_dict(spectrum)
    top_amino_acid_mass = get_top_m_elements(convolution_dict, m)

    return leaderboard_cyclopeptide_sequencing(spectrum, n, top_amino_acid_mass)

if __name__ == "__main__":
    # amino acid weight table (amino acid : weight)
    amino_acid_weight_table = {'G': 57,  'A': 71,  'S': 87,  'P': 97,  'V': 99,
                               'T': 101, 'C': 103, 'I': 113, 'N': 114, 'D': 115,
                               'K': 128, 'E': 129, 'M': 131, 'H': 137, 'F': 147,
                               'R': 156, 'Y': 163, 'W': 186}

    with open('dataset.txt') as file:
        m = int(file.readline())
        n = int(file.readline())
        spectrum = list(map(int, file.readline().split()))

    result = '-'.join([str(i) for i in convolution_cyclopeptide_sequencing(m, n, spectrum)])
    print(result)