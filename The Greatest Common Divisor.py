def GCD(a, b, *args):
    while b != 0:
        a, b = b, a % b
    for arg in args:
        while arg != 0:
            a, arg = arg, a % arg
    return a


print(GCD(24, 36, 16, 72, 144, 188))