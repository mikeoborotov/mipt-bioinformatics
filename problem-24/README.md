# Bioinformatics Algorithms (Autumn 2023) Problem 24


##  Local Alignment Problem

Find the highest-scoring local alignment between two strings.

Given: Two amino acid strings.

Return: The maximum score of a local alignment of the strings, followed by a local alignment of these strings achieving the maximum score. Use the PAM250 scoring matrix and indel penalty σ = 5. (If multiple local alignments achieving the maximum score exist, you may return any one.)


## Sample Dataset

MEANLY

PENALTY


## Sample Output

15

EANL-Y

ENALTY
