from util import primes
from itertools import dropwhile

if __name__ == '__main__':
    num = 600851475143
    p = primes.calculate_primes_till(num)
    factors = [x for x in dropwhile(lambda y: num % y, p[::-1])]
    print factors[0]
