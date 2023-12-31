# Bioinformatics Algorithms (Autumn 2023) Problem 5

We now extend “Find the Most Frequent Words with Mismatches in a String” to find frequent words with both mismatches and reverse complements. Recall that Pattern refers to the reverse complement of Pattern.


##  Frequent Words with Mismatches and Reverse Complements Problem

Find the most frequent k-mers (with mismatches and reverse complements) in a DNA string.

Given: A DNA string Text as well as integers k and d.

Return: All k-mers Pattern maximizing the sum Countd(Text, Pattern) + Countd(Text, Pattern) over all possible k-mers.


## Sample Dataset

ACGTTGCATGTCGCATGATGCATGAGAGCT

4 1


## Sample Output

ATGT ACAT