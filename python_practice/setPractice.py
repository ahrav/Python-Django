def checkMagazine(magazine, note):

    mag_dict = {x:magazine.count(x) for x in magazine}
    note_dict = {x:note.count(x) for x in note}

    for word in note_dict:
        if word in mag_dict and note_dict[word] <= mag_dict[word]:
            continue
        else:
            return "No"
    return "Yes"
    


one = ["give", "me", "one", "grand", "today"]
two = ["give", "me", "one", "grand", "today", "one"]

print (checkMagazine(one,two))