def kth_most_frequent(arr, num):
    frequency_dict = {}
    for word in arr:
        keys = frequency_dict.keys()
        if word in keys:
            frequency_dict[word] += 1
        else:
            frequency_dict[word] = 1

    index = abs(num + 1)
    if num  >= len(frequency_dict.keys()):
        return "Num greater than unique strings"
    value = sorted([y for x, y in frequency_dict.items()])[-index]
    for key, val in frequency_dict.items():
        if value == val:
            return key


words = ['i', 'am', 'am', 'i', 'eat', 'eat', 'a', 'lot', 'i']
print(kth_most_frequent({"a","b","c","a","b","a"}, 3)) 