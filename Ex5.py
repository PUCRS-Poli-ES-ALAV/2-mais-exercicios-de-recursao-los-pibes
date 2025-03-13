def is_pal(s:str) -> bool:
    if s is None:
        raise ValueError("String Nula Inserida")
    if len(s) <= 1:
        return True
    if s[0] != s[-1]:
        return False
    if s[0] == s[-1]:
        return is_pal(s[1:-1])
    return False

print(is_pal('gremio'))
