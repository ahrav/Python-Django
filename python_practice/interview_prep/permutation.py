import itertools

# Python function to print permutations of a given list 
def permutation(lst): 
    if len(lst) == 0: 
        return [] 

    if len(lst) == 1: 
        return [lst] 

    l = [] # empty list that will store current permutation 

    for i in range(len(lst)): 
       m = lst[i] 
       remLst = lst[:i] + lst[i+1:] 

       for p in permutation(remLst): 
           l.append([m] + p) 
    return l 
  
  
# Driver program to test above function 
data = list('abs') 
def print_perm(val):
    for p in permutation(val): 
        print (p) 

print_perm(data)



def to_string(a):
    return ''.join(a)

def permutation2(a, start, end):
    if start == end:
        print (to_string(a))
    else:
        for i in range(start, end+1):
            a[start], a[i] = a[i], a[start]
            permutation2(a, start+1, end)
            a[start], a[i] = a[i], a[start]


a = list('abc')
n = 3
print (permutation2(a, 0, n-1))



def all_perms(elements):
    if len(elements) <= 1:
        yield elements
    else:
        for perm in all_perms(elements[1:]):
            for i in range(len(elements)):
                # nb elements[0:1] works in both string and list contexts
                yield perm[:i] + elements[0:1] + perm[i:]

def print_perms(elements):
    for i in (all_perms(elements)):
        print (i)


print (print_perms([1,2,3]))
list(itertools.permutations([1, 6, 7]))




def permutations(elements):
    if len(elements) <= 1:
        yield elements
    for perm in permutation(elements[1:]):
        for i in range(len(elements)):
            yield perm[:i] + elements[0:1] + elements[i:]

def print_perms(elements):
    for p in permutations(elements):
        print (p)