def merge(left, right):
    """Merge sort merging function."""

    left_index, right_index = 0, 0
    result = []
    while left_index < len(left) and right_index < len(right):
        if left[left_index] < right[right_index]:
            result.append(left[left_index])
            left_index += 1
        else:
            result.append(right[right_index])
            right_index += 1

    result += left[left_index:]
    result += right[right_index:]
    return result


def merge_sort_recursive(arr):
    if len(arr) <= 1:
        return arr
    mid = len(arr) // 2
    left_half = arr[:mid]
    right_half = arr[mid:]

    return merge(merge_sort_recursive(left_half), merge_sort_recursive(right_half))




def merge_sort(arr):

    if len(arr) > 1:
        mid = len(arr)/2
        left_half = arr[:mid]
        right_half = arr[mid:]

        merge_sort(left_half)
        merge_sort(right_half)

        i = j = k = 0

        while (i < len(left_half) and j < len(right_half)):
            if left_half[i] < right_half[j]:
                arr[k] = left_half[i]
                i += 1
            else:
                arr[k] = right_half[j]
                j += 1
            k += 1

        while (i < len(left_half)):
            arr[k] = left_half[i]
            i += 1
            k += 1

        while (j < len(right_half)):
            arr[k] = right_half[j]
            j += 1
            k += 1
    return arr



arr = [4,3,2,1,6]
print (merge_sort(arr))