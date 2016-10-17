

def fib(n):
    """Выводит ряд Фибоначчи, ограниченный n."""

    a, b = 0, 1

    while b < n:
        print(b, end=' ')
        a, b = b, a + b
    print()

def fib_list(n):
    "doc momment"

    result = []
    a, b = 0, 1

    while b < n:
        result.append(b)
        a, b = b, a + b
    return result

fib(2000)

f = fib

f100 = fib_list(100)

print(f100)
