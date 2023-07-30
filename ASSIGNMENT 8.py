def count_consonants(s):
    vowels = "aeiouAEIOU"
    count = 0

    for char in s:
        if char.isalpha() and char not in vowels:
            count += 1

    return count

# Examples
print(count_consonants("Hello, World!"))  # Output: 7
print(count_consonants("The quick brown fox jumps over the lazy dog."))  # Output: 25
