def common_multiples(A, B, N):

    def nod(a, b):
        while b:
            a, b = b, a % b
        return a

    nok = A * B // nod(A, B)

    for i in range(nok, N + 1, nok):
        print(i)
