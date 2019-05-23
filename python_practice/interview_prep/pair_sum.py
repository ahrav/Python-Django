def pair_sum(arr, k):
    seen = set()
    output = set()

    for num in arr:
        target = k - num
        
        if target not in seen:
            seen.add(num)

        else:
            output.add((min(num, target), max(num, target)))

    print(map(str, list(output)))

pair_sum([1,2,3,4,5], 5)