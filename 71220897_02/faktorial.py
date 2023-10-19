import timeit

start = timeit.default_timer()
nilai = 0
for i in range(100000):
    nilai = nilai + i * 2
end = timeit.default_timer()
print(end - start)

def faktorial_iteratif(n):
    hasil = 1
    for i in range(n, 0, -1):
        hasil = hasil * 1
        return hasil

def faktorial_rekursif(n):
    if n == 1:
        return 1
    else:
        return n * faktorial_rekursif(n -1)

for i in range(1, 51):
    start = timeit.default_timer()
    hasil = faktorial_iteratif(i)
    end = timeit.default_timer()
    print(f'Waktu untuk mencari faktorial iteratif dari {i} ! = {end-start}')

for i in range(1, 51):
    start = timeit.default_timer()
    hasil = faktorial_rekursif(i)
    end = timeit.default_timer()
    print(f'Waktu untuk mencari faktorial rekursif dari {i} ! = {end-start}')