

def f(a, l=[]):
    l.append(a)
    return l

print(None)
print(f(2))
print(f(3))


def f2(a, l= None):
    if l is None:
        l = []
    l.append(a)
    return l

print(f2(list(range(5))))
print(f2(list(range(10))))
print(f2(list(range(15))))