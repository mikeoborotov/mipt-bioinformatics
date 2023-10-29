# transform DNA sequence to RNA sequence
def dna_to_rna(dna):
    return dna.replace('T', 'U')


# reverse complement of a pattern
def reverse_complement(pattern):
    # initialize result
    result = ''

    # iterate through the pattern
    for i in pattern:
        if i == 'A':
            result += 'T'
        elif i == 'C':
            result += 'G'
        elif i == 'G':
            result += 'C'
        elif i == 'T':
            result += 'A'

    return result[::-1]


# translate the peptide
def translate(rna):
    # initialize result
    peptide = ""

    # iterate through the rna
    for i in range(0, len(rna), 3):
        if rna_codon_table[rna[i:i + 3]]:
            peptide += rna_codon_table[rna[i:i + 3]]
        else:
            return peptide

    return peptide


def peptide_encoding_problem(dna, peptide):
    # initialize result
    sequence = []

    # peptide length
    peptide_len = len(peptide)

    # run through the dna
    for i in range(len(dna) - 3 * peptide_len + 1):
        if translate(dna_to_rna(dna[i:i + peptide_len * 3])) == peptide \
                or translate(dna_to_rna(reverse_complement(dna[i:i + peptide_len * 3]))) == peptide:
            sequence.append(dna[i:i + peptide_len * 3])

    return sequence


if __name__ == "__main__":
    # the dataset
    dataset = "".join(open('dataset.txt')).split()

    # rna condon table
    rna_codon_table = dict()
    with open('standard_rna_condon_table.txt') as file:
        for line in file:
            line = line.split()
            if len(line) > 1:
                rna_codon_table[line[0]] = line[1]
            else:
                rna_codon_table[line[0]] = []

    # result
    for i in peptide_encoding_problem(dataset[0], dataset[1]):
        print(i)
