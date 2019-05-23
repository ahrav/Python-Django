# from math import log
# BASE = 2

# def powersOf2(n):
#     if n < 1:
#         return 0
#     elif n == 1:
#         return 1
#     else:
#         prev = powersOf2(n/2)
#         curr = prev * 2
#         return curr

# print(powersOf2(7))
    
# def nextPowerOf2(n): 
  
#     n -= 1
#     n |= n >> 1
#     n |= n >> 2
#     n |= n >> 4
#     n |= n >> 8
#     n |= n >> 16
#     n += 1
#     return n 
  
# # Driver program to test  
# # above function  
# n = 4
# print(nextPowerOf2(2))

# print(7 - (2 ** int(log(7, 2)))

# def largestRepackaged(arrivingPackets):
#     max_val = 0
#     for x in range(len(arrivingPackets)):
#         current = (2** int(log(arrivingPackets[x], BASE)))
#         if current > max_val:
#             max_val = current
#         if x < len(arrivingPackets) -1:
#             arrivingPackets[x+1] = arrivingPackets[x+1] + (arrivingPackets[x] - current)

#     return max_val

# print(largestRepackaged([1, 2, 4, 7, 5]))



values = {'R': 0, 'P': 1, 'S': 2}
# winner = (3 + player1 - player2) % 3

def handFormationChange(n, a, formations):
    arr = list(formations)
    arr.insert(a, 'x')
    if n == 3:
        games = 2
    else:
        games = n // 2
    count = 0
    while games > 0:
        if n >= 3:
            if n % 2 == 0:
                length = n-1
            else:
                length = n-2
        else:
            length = 1

        for x in range(length):
            result = compare(arr, x, x+1, a, count)
            if result[0] == 1:
                arr = arr[:x+1] + arr[x+2:]
                n -= 1
                length -= 1
                games -= 1
                if a != 0:
                    a -= 1
            elif result[0] == 2:
                arr = arr[:x] + arr[x+1:]
                n -= 1
                length -= 1
                games -= 1
                if a != 0:
                    a -= 1
            else:
                arr = arr[:x] + arr[x+2:]
                n -= 2
                length -= 2
                games -= 2
                if a >= 2:
                    a -= 2
            count += result[1]
    return count -1 



def compare(arr, first, second, a, count):
    if first == a and arr[first] == 'x' or first == a and ((3 + values[arr[first]] - values[arr[second]]) %3 == 2 or (3 + values[arr[first]] - values[arr[second]]) %3 == 0):
        count += 1
        if arr[second] == 'R':
            arr[first] = 'P'
        if arr[second] == 'P':
            arr[first] = 'S'
        else:
            arr[first] = 'R'
    if second == a and arr[second] == 'x' or second == a and ((3 + values[arr[first]] - values[arr[second]]) %3 == 1 or (3 + values[arr[first]] - values[arr[second]]) %3 == 0):
        count += 1
        if arr[first] == 'R':
            arr[second] = 'P'
        if arr[first] == 'P':
            arr[second] = 'S'
        else:
            arr[second] = 'R'

    player1 = values[arr[first]]
    player2 = values[arr[second]]
    winner = (3 + player1 - player2) %3
    if winner == 1:
        result = (1, count)
        return result
    if winner == 2:
        result = (2, count)
        return result
    else:
        result = (0, count)
        return result

print(handFormationChange(4, 1, 'prs'))
