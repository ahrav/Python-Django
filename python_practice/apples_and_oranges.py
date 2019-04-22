def countApplesAndOranges(s, t, a, b, apples, oranges):
    good_apples = 0
    good_oranges = 0

    if a > s:
        dist_apple = abs(t-a)
    else:
        dist_apple = abs(s-a)

    if b > t:
        dist_orange = abs(b-t)
    else:
        dist_orange = abs(s-b)

    house_dist = t-s

    
    for x in apples:
        if x >= dist_apple and x <= dist_apple + house_dist:
            good_apples +=1
    for y in oranges:
        if y <= -dist_orange and y >= -dist_orange - house_dist:
            good_oranges += 1

    print (good_apples)
    print (good_oranges)
