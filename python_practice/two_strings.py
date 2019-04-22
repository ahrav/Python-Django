def twoStrings(s1, s2):

    dict_one ={x for x in s1}
    for letter in s2:
        if letter in dict_one:
            return "Yes"
    return "No"

s1 = 'hello'
s2 = 'world'

print (twoStrings(s1,s2))