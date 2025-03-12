def merge_sort(arr):
    # if the list is empty or has one element, it's already sorted
    if len(arr) <= 1:
        return arr

    # split the array into two arrays
    mid = len(arr) // 2
    left_half = arr[:mid]
    right_half = arr[mid:]

    # sort both halves
    left_half = merge_sort(left_half)
    right_half = merge_sort(right_half)

    # Merge the sorted halves
    return merge(left_half, right_half)


def merge(left, right):
    sorted_arr = []
    i = j = 0

    # Merge the two sorted arrays
    while i < len(left) and j < len(right):
        if left[i] < right[j]:
            sorted_arr.append(left[i])
            i += 1
        else:
            sorted_arr.append(right[j])
            j += 1

    # Append the remaining elements from both arrays
    sorted_arr.extend(left[i:])
    sorted_arr.extend(right[j:])

    return sorted_arr