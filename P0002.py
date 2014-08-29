from itertools import takewhile


def fibonacci():
    first = 0
    second = 1

    while True:
        first, second = second, first + second
        yield first


def even_fibonacci():
    return sum([fib for fib in takewhile(lambda num: num < 4000000, fibonacci()) if fib % 2 == 0])


if __name__ == '__main__':
    print even_fibonacci()
