def somatorio_array(arr) -> int:
    if len(arr) == 0:
        raise ValueError("Lista Vazia")
    if len(arr) == 1:
        return arr[0]
    if len(arr) == 2:
        return arr[0] + arr[1]
    return arr[0] + arr[-1] + somatorio_array(arr[1:-1])

print(somatorio_array([1,2]))