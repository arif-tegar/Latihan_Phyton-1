#1
nomor1 = 10
nomor2 = 20
nomor3 = 30

tinggi1 = 160.5
tinggi2 = 170.2
tinggi3 = 180.1

nama1 = "Andi"
nama2 = "Budi"  
nama3 = "Citra"

buah1 = ["apel", "jeruk", "mangga"]
buah2 = ["semangka", "melon", "nanas"]
buah3 = ["anggur", "kiwi", "strawberry"]

print(nomor1, nomor2, nomor3)
print(tinggi1, tinggi2, tinggi3)
print(nama1, nama2, nama3)
print(buah1, buah2, buah3)

print(type(nomor1), type(nomor2), type(nomor3))
print(type(tinggi1), type(tinggi2), type(tinggi3))
print(type(nama1), type(nama2), type(nama3))
print(type(buah1), type(buah2), type(buah3))

# 2
list_belanja = ["beras", "minyak","telur"]
list_belanja.append("gula")
list_belanja.append("kopi")

print(list_belanja)
for item in list_belanja:
    print('-',item)


#3
Harga_belanja = {'beras':12.000, 'minyak':17.000, 'telur':24.000, 'gula':15.000, 'kopi':20.000}

total = sum(Harga_belanja.values())
print(Harga_belanja)
for barang, harga in Harga_belanja.items():
    print(f"- {barang}: Rp{harga}")

print("Total harga semua belanjaan: Rp", total)

#4
def luas_keliling(panjang, lebar):
    luas = panjang * lebar
    keliling = 2 * (panjang + lebar)
    return luas, keliling

luas_keliling(10,5)[0]
jwb_luas, jwb_keliling = luas_keliling(7,4)
print(jwb_luas)
print(jwb_keliling)

#5
usia = int(input("masukan usia anda: "))
if 0 <= usia <= 13:
    print("Anak")
elif 14 <= usia <= 24:
    print ("Remaja")
elif 25 <= usia <=49:
    print("Dewasa")
elif usia >= 50:
    print("Lansia")
else:
    print("Usia tidak valid")


