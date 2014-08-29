from fractions import gcd

if __name__ == '__main__':
    print reduce(lambda x, y: x * y / gcd(x, y), range(1, 20))
