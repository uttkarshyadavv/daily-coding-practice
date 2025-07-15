def para(x, n):
    if n == 0:
        return
    print(x)
    para(x, n - 1)

para(15, 4)
