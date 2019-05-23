def unique(lst):
    
    # Initiate unique Id
    uid = 0
    
    # XOR fo revery id in id list
    for i in lst:
        
        # XOR operation
        uid ^= i
    
    return uid