# Bioinformatics Algorithms (Autumn 2023) Problem 20


##  Implement ConvolutionCyclopeptideSequencing

Given: An integer M, an integer N, and a collection of (possibly repeated) integers Spectrum.

Return: A cyclic peptide LeaderPeptide with amino acids taken only from the top M elements (and ties) of the convolution of Spectrum that fall between 57 and 200, and where the size of Leaderboard is restricted to the top N (and ties).


## Sample Dataset

20

60

57 57 71 99 129 137 170 186 194 208 228 265 285 299 307 323 356 364 394 422 493


## Sample Output

99-71-137-57-72-57

