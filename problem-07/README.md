# Bioinformatics Algorithms (Autumn 2023) Problem 7

We encountered GreedyMotifSearch in “Implement GreedyMotifSearch”. In this problem, we will power it up with pseudocounts.


##  Implement GreedyMotifSearch with Pseudocounts

Given: Integers k and t, followed by a collection of strings Dna.

Return: A collection of strings BestMotifs resulting from running GreedyMotifSearch(Dna, k, t) with pseudocounts. If at any step you find more than one Profile-most probable k-mer in a given string, use the one occurring first.


## Sample Dataset

3 5

GGCGTTCAGGCA

AAGAATCAGTCA

CAAGGAGTTCGC

CACGTCAATCAC

CAATAATATTCG



## Sample Output

TTC

ATC

TTC

ATC

TTC
