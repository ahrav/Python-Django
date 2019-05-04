def is_anagram(word1, word2):
    if len(word1) != len(word2):
        return False
    s1 = word1.lower()
    s2 = word2.lower()

    letters = {}
    for letter in s1:
        keys = letters.keys()
        if letter in keys:
            letters[letter] += 1
        else:
            letters[letter] = 1

    for letter in s2:
        keys = letters.keys()
        if letter in keys:
            letters[letter] += 1
        else:
            letters[letter] = 1
    
    for letter in letters:
        if letters[letter] % 2 != 0:
            return False
    return True

    
word1 = 'caabbb'
word2 = 'bbbaaa'

print (is_anagram(word1,word2))

# PYthon only
def anagram(w1, w2):
    if (sorted(w1) == sorted(w2)):
        return True
    return False