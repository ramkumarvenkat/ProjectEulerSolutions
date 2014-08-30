from util import primes
from itertools import dropwhile


if __name__ == '__main__':
    primes = primes.get_primes_iterator()
    n = [primes.next() for i in range(0,10001)]
    print n[-1]
