# Bioinformatics Algorithms (Autumn 2023) Problem 29


##  2-Break Sorting Problem

Find a shortest transformation of one genome into another by 2-breaks.

Given: Two genomes with circular chromosomes on the same set of synteny blocks.

Return: The sequence of genomes resulting from applying a shortest sequence of 2-breaks transforming one genome into the other.


## Sample Dataset

(+1 -2 -3 +4)

(+1 +2 -4 -3)


## Sample Output

(+1 -2 -3 +4)

(+1 -2 -3)(+4)

(+1 -2 -4 -3)

(+1 +2 -4 -3)
