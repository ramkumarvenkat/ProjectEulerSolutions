from itertools import dropwhile
from math import sqrt


def is_prime(x):
    for i in range(2, int(sqrt(x)+1)):
        if x % i == 0:
            return False
    return True


def get_primes():
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


if __name__ == '__main__':
    primes = get_primes()
    n = [primes.next() for i in range(0,10001)]
    print n[-1]
