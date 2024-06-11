def fibonacci(n):
    x, y = 0, 1
    while x <= n:
        yield x
        x, y = y, x + y