import time
import numpy as np
from BinarySearch import binary_search

start = time.time()

arr = np.array([])
for i in range(1999):
    arr = np.append(arr, np.random.randint(1, 1999))
print(f'The array: {arr}')
target = 105
result = binary_search(arr, target)

if result == -1:
    print(f'The target is: {target}')
    print("Element not found")
    print(f'Time end at: {time.time() - start}')

else:
    print(f'The target is: {target}')
    print(f'Element found at index {result}')
    print(f'Time end at: {time.time() - start}')