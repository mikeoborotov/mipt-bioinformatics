# Bioinformatics Algorithms (Autumn 2023) Problem 2

Define the skew of a DNA string Genome, denoted Skew(Genome), as the difference between the total number of occurrences of 'G' and 'C' in Genome. Let Prefix_i(Genome) denote the prefix (i.e., initial substring) of Genome of length i. For example, the values of Skew(Prefix_i("CATGGGCATCGGCCATACGCC")) are:

0 -1 -1 -1 0 1 2 1 1 1 0 1 2 1 0 0 0 0 -1 0 -1 -2


##  Minimum Skew Problem

Find a position in a genome minimizing the skew.

Given: A DNA string Genome.

Return: All integer(s) i minimizing Skew(Prefix_i(Text)) over all values of i (from 0 to |Genome|).


## Sample Dataset

CCTATCGGTGGATTAGCATGTCCCTGTACGTTTCGCCGCGAACTAGTTCACACGGCTTGATGGCAAATGGTTTTTCCGGCGACCGTAATCGTCCACCGAG


## Sample Output

53 97