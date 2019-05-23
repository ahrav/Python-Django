def non_repeating(s):
    s = s.replace(" ", "").lower()
    char_count = {}
    uniques = []
    for char in s:
        if char in char_count:
            char_count[char] += 1
        else:
            char_count[char] = 1
    for key, value in char_count.items():
        if value == 1:
            uniques.append((key, value))
    return uniques

print(non_repeating('i apple ape peels '))