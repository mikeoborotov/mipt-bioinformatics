# Bioinformatics Algorithms (Autumn 2023) Problem 25


##  Multiple Longest Common Subsequence Problem

Find a longest common subsequence of multiple strings.

Given: Three DNA strings.

Return: The maximum score of a multiple alignment of these three strings, followed by a multiple alignment of the three strings achieving this maximum. Use a scoring function in which the score of an alignment column is 1 if all three symbols are identical and 0 otherwise. (If more than one multiple alignment achieve the maximum, you may return any one.)


## Sample Dataset

ATATCCG

TCCGA

ATGTACTG


## Sample Output

3

ATATCC-G-

---TCC-GA

ATGTACTG-
