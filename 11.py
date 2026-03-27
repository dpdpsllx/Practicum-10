def isprime(n):
    if n < 2:
        return False
    for i in range(2, int(n**0.5) + 1):
        if n % i == 0:
            return False
    return True


N = int(input())

for i in range(1, N + 1):
    if isprime(i):
        print(i)
