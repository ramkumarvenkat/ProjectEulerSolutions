from util import primes
from itertools import takewhile


if __name__ == '__main__':
    print sum([n for n in takewhile(lambda num: num < 2000000, primes.get_primes_iterator())])
