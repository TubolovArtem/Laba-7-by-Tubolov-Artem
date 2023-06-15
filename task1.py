import time
import numpy as np

SIZE = 10**6

arr_1 = [np.random.rand() for _ in range(SIZE)]
arr_2 = [np.random.rand() for _ in range(SIZE)]

vanilla_time = time.perf_counter()
vanilla_arr = [arr_1[i] * arr_2[i] for i in range(SIZE)]
vanilla_time = time.perf_counter() - vanilla_time

np_time = time.perf_counter()
np_array = np.multiply(arr_1, arr_2)
np_time = time.perf_counter() - np_time

print(f"Python: {vanilla_time}")
print(f"NumPy: {np_time}")

