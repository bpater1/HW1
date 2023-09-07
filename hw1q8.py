def find_most_frequent_substring(dna):
    substring_counts = {}
    max_count = 0
    most_frequent_substrings = []

    for i in range(len(dna) - 5):
        substring = dna[i:i + 6]
        if substring in substring_counts:
            substring_counts[substring] += 1
        else:
            substring_counts[substring] = 1

        if substring_counts[substring] > max_count:
            max_count = substring_counts[substring]
            most_frequent_substrings = [i]
        elif substring_counts[substring] == max_count:
            most_frequent_substrings.append(i)

    return most_frequent_substrings

if __name__ == "__main__":
    dna_sequence = input().strip()
    indices = find_most_frequent_substring(dna_sequence)
    result = ','.join(map(str, indices))
    print(result)