#list
contoh_list = [1,2,3,4,5,6,7,7,9]
print(contoh_list)
print(len(contoh_list)) #Fungsi len() bertujuan untuk menghitung panjang atau banyaknya elemen dari list, set, dan string.

list = set([1,1,1,3,3,5,5,7,7,9,9])
print(list)
print(len(list)) #anggota list berubah menjadi anggota set yang tidak memiliki duplikat. Setelah itu, Anda mencetak jumlah anggota dari set. Hasilnya adalah anggota set berjumlah 5.

#string
list_juga = "belajar python"
print(list_juga)
print(len(list_juga)) #Perhatikan bahwa karakter space dihitung sebagai karakter string.

#min and max
#mencari anggota dengan nilai terkecil (minimal) dan nilai terbesar (maksimal) pada variabel "angka" yang merupakan list.
angka = [23,77,55,34,12,11,1,27,98]
print(min(angka))
print(max(angka))

#count
# Fungsi count() digunakan untuk mengetahui berapa kali suatu objek muncul dalam list.
genap = [2,4,4,6,6,6,10,10,8]
print("count berapa banyak:",genap.count(2))

string = "belajar bahasa anjay"
substring = "a"
print("count berapa banyak string 'a':",string.count(substring))

#in and not in
#operator yang diperuntukkan untuk mengetahui nilai atau objek yang ada dalam list
kalimat = "belajar dicoding itu menyenangkan bukan?"
print("dicoding" in kalimat)
print("?" in kalimat)
print("bukan" not in kalimat)
print("sibolga"in kalimat)

#Memberikan Nilai untuk Multiple Variable
#list atau tuple, terkadang Anda perlu memberikan nilai pada variabel-variabel tersebut. Secara konvensional, Anda bisa melakukan hal tersebut dengan menandai indeks yang diinginkan dan memberikan nilai satu per satu sesuai keinginan.
data = ["shirt","white","L"]
apparel = data[0]
color = data[1]
size = data[2]

print(data)
print(apparel)
print(color)
print(size)

#sort
#untuk mengurutkan angka atau huruf
kendaraan = ['motor','mobil','angsa','bemo','pesawat']
kendaraan.sort()
print(kendaraan)
kdraan = ['motor','mobil','angsa','bemo','pesawat']
kdraan.sort(reverse=True) #descending atau terbalik
print(kdraan) #sort tidak bisa gabungan antara str dan int, sort juga akan mendahulukan kapital

var_list = [792564, 465231, 203748, 981037, 857219, 314092, 608345, 123907, 736890, 985026, 
179430, 450218, 680934, 543187, 978260, 283045, 617902, 405826, 820913, 731095, 
592403, 109237, 874956, 605132, 214978, 674519, 391047, 825160, 509317, 768490, 
950283, 307491, 487610, 532198, 605132, 160984, 609873, 245016, 879043, 734126, 
351809, 670594, 920873, 605132, 596410, 135890, 804512, 683420, 290753, 931560, 
175430, 950672, 378490, 284105, 746098, 503624, 605132, 167432, 974810, 519463, 
407835, 740326, 281709, 630921, 953284, 605132, 429731, 183607, 369012, 541380, 
605132, 217605, 496803, 827309, 153607, 605132, 720459, 381904, 594031, 810235, 
673925, 492157, 835096, 260481, 956024, 540329, 806295, 320158, 751903, 980465, 
235780, 857943, 605132, 125094, 620493, 913250]

print("panjang",len(var_list))
print("maksimal",max(var_list))
print("minimal",min(var_list))
print("banyak",var_list.count(605132))

panjang = len(var_list)
maksimal = max(var_list)
minimal = min(var_list)
banyak = var_list.count(605132)
print("panjang",panjang)
print("maksimal",maksimal)
print("minimal",minimal)
print("banyak",banyak)

print(dict([['name','Dicoding'],['age',17]]))

x = [1, 2.2, 'Dicoding']
x[0] = 'Indonesia'
print(x)

x = 'Dicoding'
x[0] = 'F'
print(x)