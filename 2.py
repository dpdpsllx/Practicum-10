def fib(n):
    "Вывод  первых n чисел Фибоначчи😎"
    first = 1
    second = 1
    for i in range(n):
        print(first)
        nextnum = first + second
        first = second
        second = nextnum
