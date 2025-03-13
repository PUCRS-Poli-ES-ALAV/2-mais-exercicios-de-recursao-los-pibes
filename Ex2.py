def somatorio(n:int) -> int:
    if n <= 1 and n >= -1:
        return n
    if n < 0:
        return n + somatorio(n + 1)
    if n > 0:
        return n + somatorio(n - 1)
    
