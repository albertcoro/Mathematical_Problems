def is_prime(n):
    if n < 2:
        return False
    for i in range(2, int(n**0.5) + 1):
        if n % i == 0:
            return False
    return True

def marsenne_prime(x, y):
    for i in range(x, y):
        if is_prime(i) and is_prime(2**i - 1):
            print(i)

marsenne_prime(1, 100)