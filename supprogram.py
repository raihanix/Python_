# Luas pertama
panjang = 5
lebar = 10

luas_persegi_panjang = panjang * lebar
print(luas_persegi_panjang)

# Luas kedua
panjang = 4
lebar = 15

luas_persegi_panjang = panjang * lebar
print(luas_persegi_panjang)

def mencari_luas_persegi_panjang(panjang,lebar):
    luas_persegi_panjang = panjang*lebar
    return luas_persegi_panjang

persegi_panjang_pertama = mencari_luas_persegi_panjang(5,10)
print(persegi_panjang_pertama)
persegi_panjang_kedua = mencari_luas_persegi_panjang(4,15)
print(persegi_panjang_kedua)

def minimal(a, b):
    if a <= b:
        return a
    else:
        return b

#pprosedur (dalam tulisan greeting) bisa mengganti fungsi
def greeting(name):
    print("Halo " + name + ", Selamat Datang!")

greeting("Dicoding Indonesia")

def greeting():
    print("Halo Selamat Datang!")

greeting()