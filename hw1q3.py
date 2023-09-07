def transcription(dna):
    transcribed_dna = ""
    for base in dna:
        if base == 'T':
            transcribed_dna += 'U'
        else:
            transcribed_dna += base
    return transcribed_dna

if __name__ == "__main__":
    dna_input = input()
    dna_cleaned = ''.join(base for base in dna_input if base in 'ACTG')
    transcribed = transcription(dna_cleaned)
    print(transcribed)