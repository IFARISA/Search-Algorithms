from QuickSort import quick_sort
import numpy as np
import time
start = time.time()
arr = np.array([], dtype=np.int16)
for i in range(90000):
    arr = np.append(arr, np.random.randint(1, 90000))
print(quick_sort(arr))
print(f'Time end at: {time.time() - start}')