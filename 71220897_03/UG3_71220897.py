def inputtan_kata(kalimat):    
    data_kata = {}
    kata_kata = kalimat.split()
    
    for kata in kata_kata:
        huruf_awal = kata[0].lower()  
        if huruf_awal in data_kata:
            data_kata[huruf_awal].append(kata)
        else:
            data_kata[huruf_awal] = [kata]
    return data_kata

kalimat = input("Masukkan kalimat: ")

hasil = inputtan_kata(kalimat)

print(hasil)
