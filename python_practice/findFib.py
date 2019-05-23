def find_fib(number):
    if number < 2:
        return number
    return find_fib(number -1) + find_fib(number -2)

print(find_fib(6))


def fib_dynamic(number):
    answer = [0, 1]
    for i in range(number +1):
        answer.append(answer[i-1] + answer[i-2])
    return answer.pop()