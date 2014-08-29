from math import sqrt
from itertools import dropwhile


def is_prime(x):
    for i in range(2, int(sqrt(x)+1)):
        if x % i == 0:
            return False
    return True


def calculate_primes(root):
    primes = [x for x in range(3, int(sqrt(root)), 2) if is_prime(x)]
    primes.insert(0, 2)
    return primes


if __name__ == '__main__':
    num = 600851475143
    p = calculate_primes(num)
    factors = [x for x in dropwhile(lambda y: num % y, p[::-1])]
    print factors[0]
