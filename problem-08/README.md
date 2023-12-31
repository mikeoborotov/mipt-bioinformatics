# Bioinformatics Algorithms (Autumn 2023) Problem 8

We will now turn to randomized algorithms that flip coins and roll dice in order to search for motifs. Making random algorithmic decisions may sound like a disastrous idea; just imagine a chess game in which every move would be decided by rolling a die. However, an 18th Century French mathematician and naturalist, Comte de Buffon, first proved that randomized algorithms are useful by randomly dropping needles onto parallel strips of wood and using the results of this experiment to accurately approximate the constant π.

Randomized algorithms may be nonintuitive because they lack the control of traditional algorithms. Some randomized algorithms are Las Vegas algorithms, which deliver solutions that are guaranteed to be exact, despite the fact that they rely on making random decisions. Yet most randomized algorithms are Monte Carlo algorithms. These algorithms are not guaranteed to return exact solutions, but they do quickly find approximate solutions. Because of their speed, they can be run many times, allowing us to choose the best approximation from thousands of runs.

A randomized algorithm for motif finding is given below.

##  Implement RandomizedMotifSearch

Given: Positive integers k and t, followed by a collection of strings Dna.

Return: A collection BestMotifs resulting from running RandomizedMotifSearch(Dna, k, t) 1000 times. Remember to use pseudocounts!

## Sample Dataset

8 5

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
