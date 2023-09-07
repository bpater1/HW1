def optimize_mrna_sequence(amino_acid_sequence):
    codon_table = {
        "A": ["GCU", "GCC", "GCA", "GCG"],
        "C": ["UGU", "UGC"],
        "D": ["GAU", "GAC"],
        "E": ["GAA", "GAG"],
        "F": ["UUU", "UUC"],
        "G": ["GGU", "GGC", "GGA", "GGG"],
        "H": ["CAU", "CAC"],
        "I": ["AUU", "AUC", "AUA"],
        "K": ["AAA", "AAG"],
        "L": ["UUA", "UUG", "CUU", "CUC", "CUA", "CUG"],
        "M": ["AUG"],
        "N": ["AAU", "AAC"],
        "P": ["CCU", "CCC", "CCA", "CCG"],
        "Q": ["CAA", "CAG"],
        "R": ["CGU", "CGC", "CGA", "CGG", "AGA", "AGG"],
        "S": ["UCU", "UCC", "UCA", "UCG", "AGU", "AGC"],
        "T": ["ACU", "ACC", "ACA", "ACG"],
        "V": ["GUU", "GUC", "GUA", "GUG"],
        "W": ["UGG"],
        "Y": ["UAU", "UAC"],
    }

    def find_optimal_codon(amino_acid):
        codons = codon_table.get(amino_acid, [""])  # Use an empty string as a fallback
        codons.sort(key=lambda codon: (-codon.count("C"), -codon.count("G"), codon))
        return codons[0]

    # Convert the input amino acid sequence to uppercase
    amino_acid_sequence = amino_acid_sequence.upper()

    mrna_sequence = ""
    for amino_acid in amino_acid_sequence:
        if amino_acid in codon_table:
            mrna_sequence += find_optimal_codon(amino_acid)

    return mrna_sequence

import sys

# Read input amino acid sequence
amino_acid_sequence = sys.stdin.readline().strip()

# Generate and print the optimized mRNA sequence
mRNA_sequence = optimize_mrna_sequence(amino_acid_sequence)
sys.stdout.write(f'{mRNA_sequence}\n')