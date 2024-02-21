

# Binary search
def mySqrt(x: int):

    if (x == 0):
        return 0
    elif (x == 1):
        return 1

    left = 0
    right = x

    while (left <= right):
        mid = (left + right) // 2

        if (mid * mid == x):
            return mid
        elif (mid * mid > x):
            right = mid - 1
        else:
            left = mid + 1

    if (mid * mid > x):
        return mid - 1
    else:
        return mid


print(mySqrt(6))
