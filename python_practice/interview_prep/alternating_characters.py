def alternating_characters(word):
    count = 0
    for letter in range(len(word)-1):
        if word[letter] == word[letter+1]:
            count += 1
    return count

print (alternating_characters('aabbbb'))