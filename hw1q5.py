def translate_rna_codon(codon, codon_table):
    return codon_table[codon]

def count_amino_acids(rna_sequence):
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

    amino_acid_counts = {}
    
    for i in range(0, len(rna_sequence), 3):
        codon = rna_sequence[i:i+3]
        amino_acid = translate_rna_codon(codon, codon_table)
        
        if amino_acid != "" and amino_acid != "M":  # Exclude start and stop codons
            amino_acid_counts[amino_acid] = amino_acid_counts.get(amino_acid, 0) + 1

    sorted_counts = [amino_acid_counts.get(amino_acid, 0) for amino_acid in sorted(codon_table.values())]
    return sorted_counts

if __name__ == "__main__":
    rna_sequence = input().strip().upper()
    amino_acid_counts = count_amino_acids(rna_sequence)
    
    print(",".join(map(str, amino_acid_counts)))
