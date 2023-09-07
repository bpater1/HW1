def most_frequent_substring(dna):
    substr_count = {}
    max_count = 0
    max_substrings = []

    for i in range(len(dna) - 5):
        substring = dna[i:i + 6]
        if substring in substr_count:
            substr_count[substring] += 1
        else:
            substr_count[substring] = 1

        if substr_count[substring] > max_count:
            max_count = substr_count[substring]
            max_substrings = [i]
        elif substr_count[substring] == max_count:
            max_substrings.append(i)

    return max_substrings

import sys

# Read input DNA string
dna_string = sys.stdin.readline().strip()

# Get the indices of the most frequent substring and write the result to standard output
indices = most_frequent_substring(dna_string)
sys.stdout.write(','.join(map(str, indices)) + '\n')