import random
def solution(numbers, k):
    pivot = random.choice(numbers)
    number1, number2, = [], []
    for number in numbers:
        if number > pivot:
            number1.append(number)
        elif number < pivot:
            number2.append(number)
    if k <= len(number1):
        return solution(number1, k)
    if k > len(numbers) - len(number2):
        return solution(number2, k - (len(numbers) - len(number2)))
    return pivot

print(solution([5, 4, 4, 3, 2, 1], 3))