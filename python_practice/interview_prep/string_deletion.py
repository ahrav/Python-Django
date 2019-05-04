def delete(query, dictionary):
    queue = []
    queue_elements = set()
    
    queue.insert(0, query)
    queue_elements.add(query)

    while queue:
        s = queue.pop(0)
        queue_elements.remove(s)
        if s in dictionary:
            return len(query) - len(s)
        for i in range(len(s)):
            sub = s[0:i] + s[i+1, len(s)]
            if sub not in queue_elements and sub:
                queue.append(sub)
                queue_elements.add(sub)
    return -1