from typing import Callable

# Function creates dict of cache Fibonacci numbers and return function that count Fibonacci number
def caching_fibonacci() -> Callable[[int], int]:

    cache = {}
    
    # Function takes n of search Fibonacci number and return counted Fibonacci number, save cache using closure
    def fibonacci(n: int) -> int:

        if(n <= 0):
            return 0
        
        elif(n == 1):
            return 1
        
        elif(n in cache):
            return cache[n]
        
        cache[n] = fibonacci(n - 1) + fibonacci(n - 2)
        return cache[n]

    return fibonacci

print(caching_fibonacci()(15))