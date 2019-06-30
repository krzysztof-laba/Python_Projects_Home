

def fib(x0, x1, steps, max_steps):
    if steps <= max_steps:
        fib(x1, x0 + x1, steps + 1, max_steps)
        print(x0)


def fibonacci(max):
    fib(0, 1, 0, max)


fibonacci(3)
