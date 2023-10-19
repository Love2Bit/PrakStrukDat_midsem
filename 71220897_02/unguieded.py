import matplotlib.pyplot as plt
import timeit

def fibonacci_iteratif(n):
    a,b = 0,1
    for i in range(n):
        a,b = b, a+b
    return a

def fibonacci_rekursif(n):
    if n <= 1:
        return n
    else:
        return fibonacci_rekursif(n-1) + fibonacci_rekursif(n-2)
    
x = []
y = []

for i in range(1, 41):
    start = timeit.default_timer()
    hasil = fibonacci_iteratif(i)
    end = timeit.default_timer()
    x.append(i)
    y.append(end-start)
b = []

for i in range(1, 41):
    start = timeit.default_timer()
    hasil = fibonacci_rekursif(i)
    end = timeit.default_timer()
    b.append(end-start)

plt.plot(x,y)
plt.plot(x,b)
plt.xlabel('Bilangan ke-n')
plt.ylabel('Waktu')
plt.show()  