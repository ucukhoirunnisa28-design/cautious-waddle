# tugas no1
kendaraan = ["vario", "motor", 150, "pink", 2]
tambahan = [5000, "matic"]
kendaraan.extend(tambahan)
kendaraan.insert(1, "honda")
print(kendaraan)

# tugas no2
print("=== Alat hitung luas bangun datar ===")
print("pilih 1 untuk menghitung luas persegi")
print("pilih 2 untuk menghitung luas lingkaran")
print("pilih 3 untuk menghitung luas lingkaran")

pilihan = int(input("Masukan pilihan (1/2/3)"))

match pilihan:
    case 1:
        s = int(input("Masukkan panjang sisi persegi: "))
        luas = s * s
        print(f"luas persegi adalah: {luas}")
        
    case 2:
        r = int(input("Masukkan panjang jari jari lingkaran "))
        pi = 3,14
        luas = pi * r**2
        print(f"Luas lingkaran adalah: {luas}")
    case 3:
        a = int(input("Masukan panjang alas segitiga: "))
        t = int(input("Masukan panjang tingggi segitiga"))
        luas = a * t / 2
        print(f"Luas segitiga adalah: {luas}")
    case _:
        print("Masukin pilihan dengan benar")