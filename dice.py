import random

def dx(x: int) -> int:
    return random.randrange(x) + 1

def ndx(n: int, x: int) -> int:
    return sum([dx(x) for _ in range(n)])
