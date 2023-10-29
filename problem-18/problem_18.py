# peptide mass
def mass(peptide):
    mass = 0

    for i in range(len(peptide)):
        mass += amino_acid_weight_table[peptide[i]]

    return mass


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


# check if a peptide is consistent with a spectrum
def is_consistent_with_spectrum(peptide, spectrum):
    # get linear spectrum
    peptide_spectrum = linear_spectrum(peptide)

    for i in peptide_spectrum:
        if peptide_spectrum.count(i) > spectrum.count(i):
            return False
    return True


# get peptide cyclic spectrum
def cyclic_spectrum(peptide, amino_acid_weight_table):
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
            # check cyclic
            if i > 0 and j < len(peptide):
                result_spectrum.append(prefix_mass[len(peptide)] - (prefix_mass[j] - prefix_mass[i]))

    result_spectrum.append(0) # add zero to spectrum
    result_spectrum = sorted(result_spectrum)

    return result_spectrum


# problem solving
def cyclopeptide_sequencing_problem(spectrum):
    # peptide arrays
    peptides = [''] # potential peptides
    result_peptides = [] # resulting peptides

    while peptides:
        peptides = expand(peptides) # expand
        removed_peptides = [] # peptides to remove

        # run through peptides
        for i in range(len(peptides)):
            peptide = peptides[i]

            # chech id max mass
            if mass(peptide) == max(spectrum):
                if cyclic_spectrum(peptide, amino_acid_weight_table) == spectrum:
                    # if cyclic then add to result peptides
                    result_peptides.append(peptide) # add to result
                    removed_peptides.append(peptide) # remove
            elif not is_consistent_with_spectrum(peptide, spectrum):
                # if not consistent just remove
                removed_peptides.append(peptide)
        for i in range(len(removed_peptides)):
            peptides.remove(removed_peptides[i])

    result_peptide_weight = []

    # run through all selected peptides
    for peptide in result_peptides:
        # init empty
        peptide_weight = []

        # run through peptides
        for i in range(len(peptide)):
            peptide_weight.append(amino_acid_weight_table[peptide[i]])

        # append with dashes
        result_peptide_weight.append('-'.join(str(i) for i in peptide_weight))

    result = ' '.join(str(i) for i in result_peptide_weight)
    return result


if __name__ == "__main__":
    # dataset
    spectrum = list(map(int, open('dataset.txt').readline().split()))

    # amino acid weight table (amino acid : weight)
    amino_acid_weight_table = {'G': 57,  'A': 71,  'S': 87,  'P': 97,  'V': 99,
                               'T': 101, 'C': 103, 'I': 113, 'N': 114, 'D': 115,
                               'K': 128, 'E': 129, 'M': 131, 'H': 137, 'F': 147,
                               'R': 156, 'Y': 163, 'W': 186}

    print(cyclopeptide_sequencing_problem(spectrum))
