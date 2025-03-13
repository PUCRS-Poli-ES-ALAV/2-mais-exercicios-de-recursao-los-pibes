def soma_entre(i:int,j:int) -> int:
    if i == j:
        return j
    if i < j:
        return soma_entre(j,i)
    return i + soma_entre(i-1,j)

print(soma_entre(-9,10))