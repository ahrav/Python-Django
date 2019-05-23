def most_ones(n):
    arr = []
    while n > 0:
        remainder = n % 2
        n = n // 2
        arr.insert(0, remainder)

    count = 0
    most_ones = 0
    for i in arr:
        if i == 1:
            count += 1
            if count > most_ones:
                most_ones = count
        else:
            count = 0
    print(most_ones)

most_ones(6)