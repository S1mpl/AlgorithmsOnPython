def isPrime(p, max_tests):
    test = 1
    while test <= max_tests:
        if 2**(p-1) % p != 1:
            return False
        test = test + 1

    return True

print(isPrime(3463, 10000))