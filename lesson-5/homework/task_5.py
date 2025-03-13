import math
def is_prime(n):
    s = True
    for i in range(2, int(math.sqrt(n)) + 1):
        if n % i == 0:
            s = False
    return s
a = int(input())
print(is_prime(a))