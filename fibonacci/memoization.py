from math import *

def kthFibonacciUtil_Memoization(k, dp):
    # Basis: k <= 1 
    if k <=1: 
        return k

    # Case k > 1
    
    if dp[k] is not nan:
        # if we've already calculated/stored the kth fibonacci number
        return dp[k]

    # if we have NOT already calculated/stored the kth fibonacci number
    dp[k] = kthFibonacciUtil_Memoization(k - 1, dp) + kthFibonacciUtil_Memoization(k - 2, dp)

    return dp[k]

def kthFibonacciNumber_Memoization(k):
    dp = [nan] * (k + 1)
    return kthFibonacciUtil_Memoization(k, dp)