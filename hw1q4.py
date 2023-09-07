def reverse_complement(dna):
    complement = {'A': 'T', 'T': 'A', 'C': 'G', 'G': 'C'}
    return ''.join(complement[base] for base in dna[::-1])


def generate_palindromes(sequence, n, length):
    if length > n:
        return

    reverse_comp = reverse_complement(sequence)

    if sequence == reverse_comp:
        palindrome_set.add(sequence)  # Store unique palindromes

    for base in "ACGT":
        if base not in sequence:
            generate_palindromes(sequence + base, n, length + 1)


def find_palindromes(n):
    for base in "ACGT":
        generate_palindromes(base, n, 1)


if __name__ == "__main__":
    n = int(input())
    palindrome_set = set()
    find_palindromes(n)

    # Sort and print the palindromes in alphabetical order
    palindromes = sorted(palindrome_set)
    for palindrome in palindromes:
        print(palindrome)