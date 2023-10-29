# count the peptides
def count_peptides(m):
    # starting with 0
    count = 0

    # run through all amino acids
    for i in list(amino_acid_weight_table.keys()):
        if (m - amino_acid_weight_table[i]) in weight_distribution.keys():
            count += weight_distribution[(m - amino_acid_weight_table[i])]
        elif m - amino_acid_weight_table[i] < 0:
            break
        elif m - amino_acid_weight_table[i] == 0:
            count += 1
            return count
        elif m - amino_acid_weight_table[i] > 0:
            count += count_peptides(m - amino_acid_weight_table[i])
    weight_distribution[m] = count
    
    return count


if __name__ == "__main__":
    # the input
    m = 1359

    # amino acid weight table (amino acid : weight)
    amino_acid_weight_table = {'G': 57,  'A': 71,  'S': 87,  'P': 97,  'V': 99,
                               'T': 101, 'C': 103, 'I': 113, 'N': 114, 'D': 115,
                               'K': 128, 'E': 129, 'M': 131, 'H': 137, 'F': 147,
                               'R': 156, 'Y': 163, 'W': 186}
    weight_distribution = {} # initialize empty

    print(count_peptides(m))
