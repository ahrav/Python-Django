def compress(word):
    if len(word) == 1:
        return word + str(1)
    compressed_string = ''
    count = 1
    for letter in range(len(word)-1):
        if word[letter] == word[letter + 1]:
            count += 1
        else:
            compressed_string = compressed_string + word[letter] + str(count)
            count = 1
    return compressed_string + word[letter] + str(count)

word = 'a'

print (compress(word))

def compress_string(word):
    compressed_string = ''
    count = 1
    for letter in range(len(word)-1):
        if word[letter] == word[letter + 1]:
            count += 1
        else:
            compressed_string = compressed_string + word[letter] + str(count)
            count = 1
    compressed_string = compressed_string + word[len(word)-1] + str(count)
    return compressed_string

word = 'aaabbb'

print (compress_string(word))