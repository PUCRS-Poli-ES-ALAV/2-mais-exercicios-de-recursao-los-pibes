from functools import lru_cache
from time import perf_counter

# @lru_cache
def fib(n:int) -> int:
    if n < 0:
        raise ValueError('Nro deve ser Positivo')
    if n == 1 or n == 0:
        return n
    return fib(n - 1) + fib(n - 2)
start = perf_counter()
print(fib(40))
end = perf_counter()
print(start - end, "s")