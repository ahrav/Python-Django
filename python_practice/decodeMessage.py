def decode_message(word):
    cache = [None] * (len(word)+1)
    return decode_helper(word, len(word), cache)

def decode_helper(word, k, cache):
    if k == 0:
        return 1
    s = len(word) - k
    if word[s] == '0':
        return 0
    if cache[k] is not None:
        return cache[k]
    result = decode_helper(word, k-1, cache)
    if k >= 2 and int(word[s:s+2]) <= 26:
        result += decode_helper(word, k-2, cache)
    cache[k] = result
    return result


print(decode_message('121'))