def palindrome_check(word):
    for letter in range((len(word)//2)):
        if word[letter] == word[(len(word)- 1 - letter)]:
            continue
        else:
            return False
    return True

print (palindrome_check('racecar'))
print (palindrome_check([1,2,3,2,1]))


def palindrome_check2(word):
    reverse_word = reversed(word)
    True if word == reverse_word else False



## linked list
class Node:
    def __init__(self, value):
        self.value = value
        self.next = None


def is_palindrome(head):
    current = head
    runner = head
    stack = []

    while runner is not None and runner.next is not None:
        stack.append(current.value)
        current = current.next
        runner = runner.next.next
    if runner is not None:
        current = current.next
    while current is not None:
        if stack.pop() != current.value:
            return False
        current = current.next
    return True