from transaksi import Transaksi

n = int(input("Masukkan jumlah transaksi: "))

daftar_transaksi = []

for i in range(n):
    deskripsi = input(f"Masukkan deskripsi transaksi {i+1}: ")
    tanggal = input(f"Masukkan tanggal transaksi {i+1}: ")
    nominal = int(input(f"Masukkan nominal transaksi {i+1}: "))

    transaksi = Transaksi(deskripsi, tanggal, nominal)
    daftar_transaksi.append(transaksi)

total_nominal = sum([transaksi.nominal for transaksi in daftar_transaksi])

nominal_terbesar = max(daftar_transaksi, key=lambda  x: x.nominal)

print(f"Total nominal: {total_nominal}")
print(f"Nominal terbesar adalah {nominal_terbesar.nominal} pada tanggal {nominal_terbesar.tanggal}")