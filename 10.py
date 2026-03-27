def validnumber(n):
    allowed = {'1', '3', '4', '8', '9'}
    return all(d in allowed for d in str(n))


def printnumbers(A, B):
    if A > B:
        A, B = B, A

    for i in range(A, B + 1):
        if validnumber(i):
            print(i)
