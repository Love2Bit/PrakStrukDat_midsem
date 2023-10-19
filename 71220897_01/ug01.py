def menuutama():
        pilihan = 0
        while pilihan != "Q" or "q": 
            print("=====Calculator=====")
            print("Pilih Operasi :")
            print("1. Penambahan")
            print("2. Pengurangan")
            print("3. Perkalian")
            print("4. Pembagian")
            print("="*20)
            pilihan = int(input("Pilihan : "))
            if pilihan == 1 :
                x = int(input("Masukkan Bilangan Pertama : "))
                y = int(input("Masukkan Bilangan Kedua : "))
                print(x + y)
            elif pilihan == 2 :
                x = int(input("Masukkan Bilangan Pertama : "))
                y = int(input("Masukkan Bilangan Kedua : "))
                print(x - y)
            elif pilihan == 3 :
                x = int(input("Masukkan Bilangan Pertama : "))
                y = int(input("Masukkan Bilangan Kedua : "))
                print(x * y)
            elif pilihan == 4:
                x = int(input("Masukkan Bilangan Pertama : "))
                y = int(input("Masukkan Bilangan Kedua : "))
                print(x / y)
        menuutama()

menuutama()

