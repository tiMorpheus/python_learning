# fibonacci loop

a, b = 0, 1
count = 0

while b < 100:
        print(b, end=' ')
        a = b
        b = a+b
        count += 1
print("after ", count)
