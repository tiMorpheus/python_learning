import sys


print(sys.platform)
print(2 ** 100)
x = 'Spam!'
print(x * 8)


exec(open('myfile.py').read())

print(x)