#a,b,c are always 0,1,0 respectively where a and b are denoting the first two terms of fibonachi series
arr = []
def fib(a, b, count, n):
    global arr
    if count == n:
        print(arr)
        return
    arr.append(a)
    fib(b, a + b, count + 1, n)
fib(0, 1, 0, 10)
