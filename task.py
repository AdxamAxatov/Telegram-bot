def next_not_3(x: int, y: int) -> int:
    a = x * y
    if a % 3 != 0:
        return a
    else:
        a % 3 == 0
        a += 1
        return a

print(next_not_3(9, 2))
    

