# Bioinformatics Algorithms (Autumn 2023) Problem 1

Given integers L and t, a string Pattern forms an (L, t)-clump inside a (larger) string Genome if there is an interval of Genome of length L in which Pattern appears at least t times. For example, TGCA forms a (25,3)-clump in the following Genome: gatcagcataagggtcccTGCAATGCATGACAAGCCTGCAgttgttttac.


## Clump Finding Problem

Find patterns forming clumps in a string.

Given: A string Genome, and integers k, L, and t.

Return: All distinct k-mers forming (L, t)-clumps in Genome.


## Sample Dataset

CGGACTCGACAGATGTGAAGAAATGTGAAGACTGAGTGAAGAGAAGAGGAAACACGACACGACATTGCGACATAATGTACGAATGTAATGTGCCTATGGC

5 75 4


## Sample Output

CGACA GAAGA AATGT