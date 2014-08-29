from math import fabs
def sum_of_square_till_n(num):
    return (num*(num+1)*((2*num)+1))/6


def square_of_sum_till_n(num):
    sum = (num * (num+1))/2
    return sum*sum


if __name__ == '__main__':
    print fabs(sum_of_square_till_n(100) - square_of_sum_till_n(100))
