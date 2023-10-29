# Bioinformatics Algorithms (Autumn 2023) Problem 18

There are three different ways to divide a DNA string into codons for translation, one starting at each of the first three starting positions of the string. These different ways of dividing a DNA string into codons are called reading frames. Since DNA is double-stranded, a genome has six reading frames (three on each strand), as shown in Figure 1.

We say that a DNA string Pattern encodes an amino acid string Peptide if the RNA string transcribed from either Pattern or its reverse complement Pattern translates into Peptide.


##  Cyclopeptide Sequencing Problem

Given an ideal experimental spectrum, find a cyclic peptide whose theoretical spectrum matches the experimental spectrum.

Given: A collection of (possibly repeated) integers Spectrum corresponding to an ideal experimental spectrum.

Return: Every amino acid string Peptide such that Cyclospectrum(Peptide) = Spectrum (if such a string exists).


## Sample Dataset

0 113 128 186 241 299 314 427


## Sample Output

186-128-113 186-113-128 128-186-113 128-113-186 113-186-128 113-128-186

