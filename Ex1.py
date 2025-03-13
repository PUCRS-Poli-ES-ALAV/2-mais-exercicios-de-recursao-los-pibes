def fatorial(n:int) -> int:
    if n < 0:
        raise ValueError('n deve ser maior ou igual a zero')
    if n == 0:
        return 1
    return n * fatorial(n - 1)