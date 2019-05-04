a = [4,5,6,0,0,0]
b = [1,2,3]

def merge_arrays(arr1, arr2):
    if len(arr1) - len(arr2) < len(arr2):
        return "Arr1 not long enough"
    arr1_index = (len(arr1) - len(arr2)) -1
    arr2_index = len(arr2)-1
    merge_index = len(arr1)-1
    while arr1_index >= 0 and arr2_index >= 0:
        if arr1[arr1_index] > arr2[arr2_index]:
            arr1[merge_index] = arr1[arr1_index]
            arr1_index -= 1
        else:
            arr1[merge_index] = arr2[arr2_index]
            arr2_index -= 1
        merge_index -=1
    while arr2_index >= 0:
        arr1[merge_index] = arr2[arr2_index]
        merge_index -= 1
        arr2_index -= 1
    return arr1

print (merge_arrays(a, b))