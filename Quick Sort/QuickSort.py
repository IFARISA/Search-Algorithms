def quick_sort(arr):
    # if the list is empty or has one element, it's already sorted
    if len(arr) <= 1:
        return arr

    # last element as pivot
    pivot = arr[-1]

    # left smaller than or equal to the pivot, right is greater than the pivot
    left = [x for x in arr[:-1] if x <= pivot]
    right = [x for x in arr[:-1] if x > pivot]

    # apply quick sort
    return quick_sort(left) + [pivot] + quick_sort(right)



