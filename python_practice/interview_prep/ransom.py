def check_magazine(magazine, note):
    dict1 = {}
    value = ''
    for word in magazine:
        if word in dict1.keys():
            dict1[word] += 1
        else:
            dict1[word] = 1
    
    for word in note:
        if word in dict1.keys():
            if dict1[word] == 0:
                value = "No"
            else:
                dict1[word] -= 1
        else:
            value = "No"
    if len(value):
        print ("No")
    else:
        print ("Yes")


str1 = "give me one grand today night"
str2 = "give one grand today"

print (check_magazine(str1,str2))