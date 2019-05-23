def reverse(string):
    if type(string) is not str or not string or len(string) < 2:
        return "You done goofed"
    string = string.split()
    return " ".join(string[::-1])

def reverse2(string):
    if type(string) is not str or not string or len(string) < 2:
        return "You done goofed"
    return string[::-1]

print(reverse(1))
print(reverse2('hello man whats up'))
print(reverse('hello man whats up'))