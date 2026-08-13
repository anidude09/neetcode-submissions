class Solution:
    def tribonacci(self, n: int) -> int:



        count = 0
        cache = {}

        def fib(n):
            nonlocal count
            if n == 0:
                return 0
            if n == 1 or n == 2:
                return 1
            if n in cache:
                return cache[n]

            cache[n] = fib(n-1) + fib(n-2) + fib(n-3)

            return cache[n]
        
        return fib(n)
        