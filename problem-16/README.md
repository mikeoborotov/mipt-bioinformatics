# Bioinformatics Algorithms (Autumn 2023) Problem 16

There are three different ways to divide a DNA string into codons for translation, one starting at each of the first three starting positions of the string. These different ways of dividing a DNA string into codons are called reading frames. Since DNA is double-stranded, a genome has six reading frames (three on each strand), as shown in Figure 1.

We say that a DNA string Pattern encodes an amino acid string Peptide if the RNA string transcribed from either Pattern or its reverse complement Pattern translates into Peptide.


##  Peptide Encoding Problem

Find substrings of a genome encoding a given amino acid sequence.

Given: A DNA string Text and an amino acid string Peptide.

Return: All substrings of Text encoding Peptide (if any such substrings exist).


## Sample Dataset

ATGGCCATGGCCCCCAGAACTGAGATCAATAGTACCCGTATTAACGGGTGA

MA


## Sample Output

ATGGCC

GGCCAT

ATGGCC
