# Bioinformatics Algorithms (Autumn 2023) Problem 10

The first potential issue with implementing MedianString from “Find a Median String” is writing a function to compute d(Pattern, Dna) = ∑ti=1 d(Pattern, Dnai), the sum of distances between Pattern and each string in Dna = {Dna1, ..., Dnat}.


##  Compute DistanceBetweenPatternAndStrings

Find the distance between a pattern and a set of strings.

Given: A DNA string Pattern and a collection of DNA strings Dna.

Return: DistanceBetweenPatternAndStrings(Pattern, Dna).


## Sample Dataset

AAA

TTACCTTAAC GATATCTGTC ACGGCGTTCG CCCTAAAGAG CGTCAGAGGT


## Sample Output

5