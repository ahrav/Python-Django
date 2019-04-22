def birthdayCakeCandles(ar):
    count = 0
    max = ar[0]

    for x in ar:
        if x > max:
            max = x
            count = 1
        elif x == max:
            count += 1
        else:
            continue
    return count

ar = [1,2,3,4,5,5,6,6,6]
birthdayCakeCandles(ar)


# dict = {x:ar.count(x) for x in ar}
#     max_val = max(dict.keys())
#     print (len(dict))
#     print (dict[max_val])