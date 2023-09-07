def count_amino_acids(rna_sequence):
    codon_table = {
        "UUU": "F", "UUC": "F", "UUA": "L", "UUG": "L",
        "UCU": "S", "UCC": "S", "UCA": "S", "UCG": "S",
        "UAU": "Y", "UAC": "Y", "UAA": "STOP", "UAG": "STOP",
        "UGU": "C", "UGC": "C", "UGA": "STOP", "UGG": "W",
        "CUU": "L", "CUC": "L", "CUA": "L", "CUG": "L",
        "CCU": "P", "CCC": "P", "CCA": "P", "CCG": "P",
        "CAU": "H", "CAC": "H", "CAA": "Q", "CAG": "Q",
        "CGU": "R", "CGC": "R", "CGA": "R", "CGG": "R",
        "AUU": "I", "AUC": "I", "AUA": "I", "AUG": "M",
        "ACU": "T", "ACC": "T", "ACA": "T", "ACG": "T",
        "AAU": "N", "AAC": "N", "AAA": "K", "AAG": "K",
        "AGU": "S", "AGC": "S", "AGA": "R", "AGG": "R",
        "GUU": "V", "GUC": "V", "GUA": "V", "GUG": "V",
        "GCU": "A", "GCC": "A", "GCA": "A", "GCG": "A",
        "GAU": "D", "GAC": "D", "GAA": "E", "GAG": "E",
        "GGU": "G", "GGC": "G", "GGA": "G", "GGG": "G",
    }

    amino_acid_counts = {
        "F": 0, "L": 0, "S": 0, "Y": 0, "STOP": 0,
        "C": 0, "W": 0, "P": 0, "H": 0, "Q": 0,
        "R": 0, "I": 0, "M": 0, "T": 0, "N": 0,
        "K": 0, "V": 0, "A": 0, "D": 0, "E": 0, "G": 0
    }

    for i in range(0, len(rna_sequence), 3):
        codon = rna_sequence[i:i + 3]
        amino_acid = codon_table.get(codon, "X")  # Use "X" for undefined codons
        amino_acid_counts[amino_acid] += 1

    return amino_acid_counts

if __name__ == "__main__":
    rna_sequence = input()
    amino_acid_counts = count_amino_acids(rna_sequence)

    # Print the counts in lexicographic order
    amino_acids = ["F", "L", "S", "Y", "STOP", "C", "W", "P", "H", "Q", "R", "I", "M", "T", "N", "K", "V", "A", "D", "E", "G"]
    counts = [str(amino_acid_counts[acid]) for acid in amino_acids]
    print(",".join(counts))