def heapify(arr, n, i):
    largest = i
    left = 2 * i + 1
    right = 2 * i + 2

    # if left child is larger than root
    if left < n and arr[left] > arr[largest]:
        largest = left

    # if right child is larger than largest so far
    if right < n and arr[right] > arr[largest]:
        largest = right

    # if largest is not root
    if largest != i:
        arr[i], arr[largest] = arr[largest], arr[i]  # Swap

        # Recursively heapify the affected subtree
        heapify(arr, n, largest)

def heap_sort(arr):
    n = len(arr)

    # build a max heap
    for i in range(n // 2 - 1, -1, -1):
        heapify(arr, n, i)

    # extract elements one by one from the heap
    for i in range(n - 1, 0, -1):
        arr[i], arr[0] = arr[0], arr[i]  # swap the root (max element) with the last element
        heapify(arr, i, 0)  # heapify the reduced heap

    return arr