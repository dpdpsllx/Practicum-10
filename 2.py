def fib(n):
    first = 1
    second = 1
    for i in range(n):
        print(first)
        nextnum = first + second
        first = second
        second = nextnum
