def transcription(dna):
    transcribed_dna = ""
    count = 0

    for base in dna:
        if base == 'T':
            transcribed_dna += 'U'
        else:
            transcribed_dna += base

        if base.isalpha():  # Check if the character is alphabetic (A, C, G, or T)
            count += 1

        if count % 3 == 0 and count != len(dna):
            transcribed_dna += '-'

    return transcribed_dna

if __name__ == "__main__":
    dna_input = input().upper()
    transcribed = transcription(dna_input)
    print(transcribed)
