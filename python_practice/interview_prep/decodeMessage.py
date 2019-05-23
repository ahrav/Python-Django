def num_ways(string):
    cache = [None] * (len(string) + 1)
    return num_ways_helper(string, len(string), cache)

def num_ways_helper(string, length, cache):
    if length == 0:
        return 1
    s = len(string) - length
    if string[s] == '0':
        return 0
    if cache[length] is not None:
        return cache[length]
    result = num_ways_helper(string, length-1, cache)
    if length >=2 and int(string[s:s+2]) <= 26:
        result += num_ways_helper(string, length-2, cache)
    cache[length] = result
    return result

print(num_ways('111'))