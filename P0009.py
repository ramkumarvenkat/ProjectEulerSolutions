if __name__ == '__main__':
    for x in range(333, 0, -1):
        for y in range(333, 666):
            for z in range(333, 1001):
                if z ** 2 == x ** 2 + y ** 2 and x + y + z == 1000:
                    print x, y, z, x*y*z
                    break
