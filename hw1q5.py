def translate_rna_codon(codon, codon_table):
    return codon_table[codon]

def count_amino_acids(rna_sequence):
    codon_table = {
    "GCU": "A", "GCC": "A", "GCA": "A", "GCG": "A",
    "UGU": "C", "UGC": "C",
    "GAU": "D", "GAC": "D",
    "GAA": "E", "GAG": "E",
    "UUU": "F", "UUC": "F",
    "GGU": "G", "GGC": "G", "GGA": "G", "GGG": "G",
    "CAU": "H", "CAC": "H",
    "AUU": "I", "AUC": "I", "AUA": "I",
    "AAA": "K", "AAG": "K",
    "UUA": "L", "UUG": "L", "CUU": "L", "CUC": "L", "CUA": "L", "CUG": "L",
    "AUG": "M",
    "AAU": "N", "AAC": "N",
    "CCU": "P", "CCC": "P", "CCA": "P", "CCG": "P",
    "CAA": "Q", "CAG": "Q",
    "CGU": "R", "CGC": "R", "CGA": "R", "CGG": "R", "AGA": "R", "AGG": "R",
    "UCU": "S", "UCC": "S", "UCA": "S", "UCG": "S", "AGU": "S", "AGC": "S",
    "ACU": "T", "ACC": "T", "ACA": "T", "ACG": "T",
    "GUU": "V", "GUC": "V", "GUA": "V", "GUG": "V",
    "UGG": "W",
    "UAU": "Y", "UAC": "Y",
    "UAA": "STOP", "UAG": "STOP", "UGA": "STOP",
}

    amino_acid_counts = {}
    
    for i in range(0, len(rna_sequence), 3):
        codon = rna_sequence[i:i+3]
        amino_acid = translate_rna_codon(codon, codon_table)
        
        if amino_acid != "":
            amino_acid_counts[amino_acid] = amino_acid_counts.get(amino_acid, 0) + 1

    sorted_counts = [amino_acid_counts.get(amino_acid, 0) for amino_acid in sorted(codon_table.values())]
    return sorted_counts

if __name__ == "__main__":
    rna_sequence = input().strip().upper()
    amino_acid_counts = count_amino_acids(rna_sequence)
    
    print(",".join(map(str, amino_acid_counts)))
