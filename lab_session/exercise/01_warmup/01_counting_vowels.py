def count_vowels(string: str) -> int:
    """Return the number of vowels in the given string"""
    vowels = ('a', 'e', 'i', 'o', 'u', 'A', 'E', 'I', 'O', 'U')
    count_vow = 0

    for letter in string:
        if letter in vowels:
            count_vow += 1
    return count_vow

print(count_vowels("mathematics"))





