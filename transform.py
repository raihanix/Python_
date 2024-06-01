# kata = 'monyet'
# kata = kata.upper()
# print(kata)

# perintah = 'SERIGALA'
# perintah = perintah.lower()
# print(perintah)

# print("haloo       ".rstrip()) #right strip 
# print("      haloo".lstrip()) #left strip
# print("      haloo       ".strip()) #middle strip

# sebut = 'nininininimonyetnononono'
# print(sebut.strip("nino")) #strip bisa digunakan untuk menghapus kata dalam kalimat

# print('monyet luar angkasa'.startswith('monyet')) # bertujuan untuk menemukan suatu kata pada awal string.
# print('monyet luar angkasa'.endswith('monyet')) # bertujuan untuk menemukan suatu kata pada akhir string.

# #join()
# print(' '.join(['monyet','luar angkasa','itu ada','?'])) #menggabungkan string yang telah disimpan pada variabel list.
# print('dih'.join(['monyet','lairangkoso']))

# #split() menguraikan string yang ada di kalimat
# print('monyet luar angkasa'.split())

# print('''halo,
#       aku suka ikan manis
#       tapi kamu suka ayam pait ga?'''.split('\n'))

#replace, mengganti elemen string dengan elemen string lainnya
kata = "ayo kita main layangan merah"
print(kata.replace("merah","biru"))

#isupper(), akan mengembalikan nilai True jika semua huruf dalam string adalah huruf kapital (uppercase)
kalimat = "GAJAH BESAR" #mengecek seluruh huruf dalam huruf besar
sebut = "monyet123"
print(kalimat.isupper())
print(kata.islower()) #mengecek apakah seluruh huruf dalam huruf kecil
print(kalimat.isalpha()) #mengecek apakah seluruh kata itu tidak memiliki selain alphabet(termasuk spasi)
print(sebut.isalnum()) #mengembalikan nilai True jika karakter dalam string adalah alfanumerik, yaitu hanya huruf atau hanya angka atau berisi keduanya
print("1231".isdecimal()) #kan mengembalikan nilai True jika karakter dalam string berisi hanya angka/numerik
print("   ".isspace()) #akan mengembalikan nilai True jika string hanya berisi whitespace, seperti spasi, tab, newline, atau karakter whitespace lainnya.
print("Gajah besar".istitle())# mengecek apakah awal huruf, huruf besar

#zfill (Metode zfill() bertujuan untuk menambahkan nilai nol (0) di depan sebuah string dengan panjang tertentu. 
#Tujuan dari metode ini adalah membantu untuk memastikan bahwa sebuah angka atau nilai memiliki panjang tetap, 
#terutama ketika ingin menyimpan nilai dalam format yang konsisten.)
teks = 'code'
tambah_number = teks.zfill(6)
print(tambah_number)

print("Monyet".rjust(10)) #menambah spasi diawal huruf
print("Monyet".ljust(10)) #menambah spasi diakhir huruf
print("Monyet".center(10, '-')) #membuat karakter ditengah
print("jum'at")
print("Halo!\nKapan terakhir kali kita bertemu?\nKita bertemu hari Jum\'at yang lalu.")