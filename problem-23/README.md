# Bioinformatics Algorithms (Autumn 2023) Problem 23


##  Global Alignment Problem

Find the highest-scoring alignment between two strings using a scoring matrix.

Given: Two amino acid strings.

Return: The maximum alignment score of these strings followed by an alignment achieving this maximum score. Use the BLOSUM62 scoring matrix and indel penalty σ = 5. (If multiple alignments achieving the maximum score exist, you may return any one.)


## Sample Dataset

PLEASANTLY

MEANLY


## Sample Output

8

PLEASANTLY

-MEA--N-LY
