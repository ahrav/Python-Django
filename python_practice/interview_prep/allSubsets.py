def all_subsets(arr):
    subset = [None] * len(arr)
    subset_helper(arr, subset, 0)

def subset_helper(arr, subset, i):
    if i == len(arr):
        print_set(subset)
    else:
        subset[i] = None
        subset_helper(arr, subset, i +1)
        subset[i] = arr[i]
        subset_helper(arr, subset, i +1)

def print_set(subset):
    out = (map(lambda x : x, subset))
    print(filter(lambda val: val is not None, out))

print(all_subsets([1,2,3]))