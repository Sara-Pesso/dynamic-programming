from math import *

def kthFibonacciNumber_Tabulation(k):
    # Initialize the Fibonacci Numbers: [0,1]
    if k <= 1:
        return k

    dp = [nan] * (k + 1)
    dp[0], dp[1] = 0, 1

    # Solve up to k
    for i in range(2, k + 1):
        dp[i] = dp[i-1] + dp[i-2]

    return dp[k]

def kthFibTabulation_OptimizedSpace(k):
    if k <= 1: 
        return k

    # Store only the current Fibonacci number, instead of all k Fibonacci numbers
    current_fib = 0 

    # Initialize the first two Fibonacci numbers: [0,1]
    previous_fibs = [0,1]

    for _ in range(2, k + 1):
        current_fib = previous_fibs[0] + previous_fibs[1]

        #Update!
        previous_fibs = [previous_fibs[1], current_fib]

    return current_fib
