
a = ['cat', 'window', 'compiler']

print(a)

for x in a[:]:
    if len(x) > 6:
        a.insert(0, x)

print(a)

for i in range(5):
    print(i)                # 0, 1, 2, 3,

for i in range(5, 10):
    print(i)                # 5, 6, 7, 8, 9

for i in range(5, 20, 2):
    print(i)                # 5 , 7 , 9 ... 19

for i in range(len(a)):
    print(i, a[i])


print(list(range(10)))
