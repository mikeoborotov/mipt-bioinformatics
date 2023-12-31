# Bioinformatics Algorithms (Autumn 2023) Problem 9

We have previously defined the notion of a Profile-most probable k-mer in a string. We now define a Profile-randomly generated k-mer in a string Text. For each k-mer Pattern in Text, compute the probability Pr(Pattern | Profile), resulting in n = |Text| - k + 1 probabilities (p1, …, pn). These probabilities do not necessarily sum to 1, but we can still form the random number generator Random(p1, …, pn) based on them. GIBBSSAMPLER uses this random number generator to select a Profile-randomly generated k-mer at each step: if the die rolls the number i, then we define the Profile-randomly generated k-mer as the i-th k-mer in Text.


##  Implement GibbsSampler

Given: Integers k, t, and N, followed by a collection of strings Dna.

Return: The strings BestMotifs resulting from running GibbsSampler(Dna, k, t, N) with 20 random starts. Remember to use pseudocounts!


## Sample Dataset

8 5 100

CGCCCCTCTCGGGGGTGTTCAGTAAACGGCCA

GGGCGAGGTATGTGTAAGTGCCAAGGTGCCAG

TAGTACCGAGACCGAAAGAAGTATACAGGCGT

TAGATCAAGTTTCAGGTGCACGTCGGTGAACC

AATCCACCAGCTCCACGTGCAATGTTGGCCTA


## Sample Output

TCTCGGGG

CCAAGGTG

TACAGGCG

TTCAGGTG

TCCACGTG
