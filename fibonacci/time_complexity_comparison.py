import timeit
from memoization import *
from tabulation import *
from recursion import *

# Testing the time complexity
k = 100
runs = 100000

# total_time_recursion = timeit.timeit('kthFibonacci_Recursion(k)', globals=globals(), number=runs)
# print(f"Average Recursion Time: {total_time_recursion/runs:.7f} seconds")

total_time_memoization = timeit.timeit('kthFibonacciNumber_Memoization(k)', globals=globals(), number=runs)
print(f"Average Memoization (Top-Down) Time: {total_time_memoization/runs:.7f} seconds")

total_time_tabulation = timeit.timeit('kthFibonacciNumber_Tabulation(k)', globals=globals(), number=runs)
print(f"Average Tabulation (Bottom-Up) Time: {total_time_tabulation/runs:.7f} seconds")

total_time_tabulation_opt = timeit.timeit('kthFibTabulation_OptimizedTime(k)', globals=globals(), number=runs)
print(f"Average Tabulation Optimized (Bottom-Up) Time: {total_time_tabulation_opt/runs:.7f} seconds")