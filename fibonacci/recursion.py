def kthFibonacci_Recursion(n):
    
    # base case
    if n <= 1:
        return n
      
    # sum of the two preceding 
    # Fibonacci numbers
    return kthFibonacci_Recursion(n - 1) + kthFibonacci_Recursion(n - 2)