# Bioinformatics Algorithms (Autumn 2023) Problem 6

##  Implement GreedyMotifSearch

Given: Integers k and t, followed by a collection of strings Dna.

Return: A collection of strings BestMotifs resulting from running GreedyMotifSearch(Dna, k, t). If at any step you find more than one Profile-most probable k-mer in a given string, use the one occurring first.


## Sample Dataset

3 5

GGCGTTCAGGCA

AAGAATCAGTCA

CAAGGAGTTCGC

CACGTCAATCAC

CAATAATATTCG

## Sample Output

CAG

CAG

CAA

CAA

CAA
