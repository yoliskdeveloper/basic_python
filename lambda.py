# anonymous function atau lambda
x = lambda a : a ** 2
print(x(10))

# dengan banyak argument
x = lambda a, b: a * b
print(x(12, 24))

x = lambda p, l, t : print('panjang persegi:', p * l * t)
x(12, 12, 45)

# lambda di dalam function
def my_funct(n):
    return lambda a : a * n

mydoubler = my_funct(2)
print(mydoubler(11))
