from math import sqrt

def is_prime(x):
    for i in range(2, int(sqrt(x)+1)):
        if x % i == 0:
            return False
    return True

def is_prime(x):
    for i in range(2, int(sqrt(x)+1)):
        if x % i == 0:
            return False
    return True


def calculate_primes_till(root):
    primes = [x for x in range(3, int(sqrt(root)), 2) if is_prime(x)]
    primes.insert(0, 2)
    return primes


def get_primes_iterator():
    yield 2
    n = 1
    while True:
        candidate = (4 * n) - 1
        if is_prime(candidate):
            yield candidate
        candidate = (4 * n) + 1
        if is_prime(candidate):
            yield candidate
        n += 1