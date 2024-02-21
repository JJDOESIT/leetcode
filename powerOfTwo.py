

def isPowerOfTwo(n: int):
    power = 0
    while (2 ** power <= n):
        if 2 ** power == n:
            return True
        power += 1

    return False


print(isPowerOfTwo(16))
