def is_palindrome(num):
    string = str(num)
    for i in range(0, int(len(string)/2)):
        if string[i] != string[len(string) - 1 - i]:
            return False
    return True


def find_largest_palindrome(min, max):
    max_palindrome = -1
    for i in range(min,max):
        for j in range(max,min,-1):
            product = i*j
            if is_palindrome(product) and product > max_palindrome:
                max_palindrome = product
    return max_palindrome

if __name__ == '__main__':
    print find_largest_palindrome(100,999)
