import json

def load_data(filename):
    try:
        with open(filename, 'r') as file:
            return json.load(file)
    except FileNotFoundError:
        return {}

def simpan_data(data, filename):
    with open(filename, 'w') as file:
        json.dump(data, file, indent=2)

def viewDataBelanja(data):
    total_nominal = 0
    print("\nDaftar Belanja:")
    for i, (catatan, nominal) in enumerate(data.items(), start=1):
        total_nominal += nominal
        print(i, catatan, '- Rp ', nominal)
    print('Total Nominal: Rp ',total_nominal, "\n")

filename = "belanja.json"
data_belanja = load_data(filename)

viewDataBelanja(data_belanja)

while True:
    catatan = input("Masukkan catatan: ")
    if not catatan:
        break

    try:
        nominal = int(input("Masukkan nominal: "))
    except ValueError:
        print("Nominal harus berupa angka. Silakan coba lagi.")


    data_belanja[catatan] = data_belanja.get(catatan, 0) + nominal
    simpan_data(data_belanja, filename)
    print("Data berhasil tersimpan!\n")
    viewDataBelanja(data_belanja)
    break