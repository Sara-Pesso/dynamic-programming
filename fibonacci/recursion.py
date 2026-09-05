def kthFibonacci_Recursion(n):
    
    # basis and termination criteria
    if n <= 1:
        return n
      
    # sum of the two preceding Fibonacci numbers: F(n) = F(n-1) + F(n-2)
    return kthFibonacci_Recursion(n - 1) + kthFibonacci_Recursion(n - 2)
