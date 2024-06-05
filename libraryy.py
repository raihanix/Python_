# testString = "dicoding"
# testString.upper()
# print(testString.upper())

# '''
# upper(): Ubah setiap huruf dalam string menjadi huruf kapital. 
# lower(): Ubah setiap huruf dalam string menjadi huruf kecil.
# split(): Pisahkan teks berdasarkan delimiter (karakter pemisah).
# title(): Jadikan setiap awal kata kapital.
# zfill(): Tambahkan nol di awal string sebanyak nilai yang ada pada parameter.
# '''

# '''
# regex berfungsi untuk mencari kata atau kumpulan kata dengan memberikan pola yan gdiinginkan
# '''

# import re
# pola= 'a...s$'
# string_test= 'abyss'
# hasil= re.match(pola, string_test)

# if hasil:
#     print("berhasil")

# else:
#     print("gagal")

# '''
# library matematika
# '''
# import math

# print(math.sqrt(25)) 
# print(math.pi) 

# '''library parser
#  untuk menguraikan kode Python menjadi struktur data yang dapat diproses dan dianalisis. 
#  Argument parser bermanfaat jika kita ingin membuat program atau skrip kecil yang langsung 
#  menerima parameter pada saat pemanggilan program. Hal ini biasa digunakan dalam 
#  pemanggilan aplikasi atau skrip di CLI/terminal *nix-based, misalnya Linux dan MacOS. 
# '''
# import argparse
 
# parser = argparse.ArgumentParser()
# parser.add_argument('-o', '--output', action='store_true', help="tampilkan output")
# args = parser.parse_args()
 
# if args.output:
#    print("Halo, ini merupakan sebuah output dari panggildicoding.py")

# '''
# pandas adalah library untuk mengelola dan analisis data
# '''
# import pandas as pd
#     #membuat dataframe dari dictionary
# data = {
#             'nama':['john','jane','bob','alice'],
#             'usia':[25,30,22,28],
#             'pekerjaan':['engineer','teacher','designer','doctor']
# }
# df = pd.DataFrame(data)
#     #menampilkan dataframe
# print(df)

# '''
# library untuk melakukan visualisasi data. Matplotlib termasuk jenis 
# library eksternal sehingga Anda perlu melakukan instalasi matplotlib terlebih dahulu.
# '''
# import matplotlib.pyplot as plt
 
# # Data
# x = [1, 2, 3, 4, 5]
# y = [2, 4, 6, 9, 10]
 
# # Membuat plot garis
# plt.plot(x, y)
 
# # Menambahkan judul dan label sumbu
# plt.title("Contoh Plot Garis")
# plt.xlabel("Sumbu X")
# plt.ylabel("Sumbu Y")
 
# # Menampilkan plot
# plt.show()

# '''
# library dengan tujuan untuk visualisasi data sama seperti matplotlib. 
# Bahkan library seaborn dibangun berdasarkan pada library matplotlib.
# '''
# import seaborn as sns
# import matplotlib.pyplot as plt
 
# # Contoh data
# tips = sns.load_dataset('tips')  # Memuat dataset tips dari Seaborn
 
# # Contoh plot histogram
# sns.histplot(tips['total_bill'], kde=True)
# plt.title('Histogram Total Bill')
# plt.xlabel('Total Bill')
# plt.ylabel('Frequency')
# plt.show()

'''
OS pada Python berguna untuk fungsi-fungsi yang berkaitan dengan sistem 
operasi, misalnya open(), path(), getcwd(), dan fungsi lainnya. Modul 
ini memungkinkan Anda untuk memanfaatkan fungsi yang sama dan mengeksekusi 
fungsi terkait OS yang mungkin berbeda dalam setiap sistem operasi.
'''
import os
print(os.getcwd())
'''
pickle
Jika Anda memiliki sebuah list yang ingin disimpan atau ditransmisikan 
tanpa khawatir bentuknya akan rusak atau kacau, fungsi dari library pickle 
dapat dimanfaatkan. Pickle termasuk fungsi Object Serialization pada Python. 
Pickling adalah istilah untuk mengubah objek menjadi byte stream, sedangkan 
unpickling adalah perlakuan sebaliknya.
'''
import pickle
contoh_dictionary = {1:"6", 2:"2", 3:"f"}
pickle_keluar = open("dict.pickle","wb")
pickle.dump(contoh_dictionary, pickle_keluar)
pickle_keluar.close()

import pickle
pickle_masuk = open("dict.pickle", "rb")
contohDictionary = pickle.load(pickle_masuk)
pickle_masuk.close()
 
print(contohDictionary)

'''
Beautifulsoup adalah library untuk mengambil 
data dari halaman web dan mengekstrak informasi yang diperlukan.
 Hal pertama yang dilakukan adalah mengimpor Beautifulsoup sebagai 
 library yang akan kita gunakan. Selanjutnya kita mengambil konten 
 dari url dengan menggunakan fungsi dari modul “urlopen”. Setelah konten 
 diambil, kita membuat objek BeautifulSoup dan dari objek ini kita bisa 
 memunculkan beberapa konten berdasarkan tag html. Pada contoh di atas, 
 kita mengambil judul halaman dengan menggunakan method “title”.
'''
from urllib.request import urlopen
from bs4 import BeautifulSoup
 
# Pengambilan konten
url = "http://python.org/"
page = urlopen(url)
html = page.read().decode("utf-8")
 
# Membuat objek BeautifulSoup
soup = BeautifulSoup(html, "html.parser")
 
# Mencetak judul halaman
print(soup.title)
'''
Urllib adalah library bawaan dari Python yang bertujuan untuk scraping 
konten dari sebuah website. Penggunaan urllib berbeda dengan beautifulsoup. 
Bisa dikatakan bahwa cara penggunaan urllib sedikit kompleks dibandingkan 
beautifulsoup. Kode di bawah adalah contoh untuk memulai proses scraping 
pada situs dengan domain python.org dan menampilkan isi dari tag title dari 
situs tersebut.
'''

from urllib.request import urlopen
 
# Pengambilan konten
url = "http://python.org/"
page = urlopen(url)
html = page.read().decode("utf-8")
 
# Mencari indeks awal dan akhir
start_index = html.find("<title>") + len("<title>")
end_index = html.find("</title>")
 
# Mengekstrak dan mencetak judul halaman
title = html[start_index:end_index]
print(title)