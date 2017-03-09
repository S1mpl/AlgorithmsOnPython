def GCD(a, b):
    while b != 0:
        remainder = a % b
        a = b
        b = remainder
    return a

#example
print(GCD(4851,3003))