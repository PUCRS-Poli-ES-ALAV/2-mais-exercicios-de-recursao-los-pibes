def conv_base2(n:int) -> str:
    if n < 0:
        raise ValueError('Nro nao deve ser negativo')
    if n == 0:
        return '0'
    if n == 1:
        return '1'
    return conv_base2(n // 2) + str(n%2)

print(conv_base2(10))