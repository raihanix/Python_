class Mobil:
    # pass #karena belum mendefinisikan atribut dan metode pernyataan pass ini agar tidak error
    warna = "merah"

mobil_1 = Mobil()
mobil_1.warna = "biru"
print(mobil_1.warna) #mobil_1 sebagai objek dan warna sebagai atribut

mobil_2 = Mobil()
print(mobil_2.warna)

mobil_3 = Mobil()
print(mobil_3.warna)

print("-------------")
#mengubah atribut kelas

Mobil.warna = "hitam"

print(mobil_1.warna)
print(mobil_2.warna)
print(mobil_3.warna)

'''Class constructor
menentukan nilai awal atau kondisi awal dari suatu kelas
Dengan fungsi ini, saat kita melakukan proses instansiasi atau pembuatan objek baru, 
hal pertama yang dilakukan adalah memanggilnya terlebih dahulu.'''

print("-------------")
class Mobil:
    #atribut Instance
    def __init__(self): #sebagai fungsi khusus untuk menjadi constructor
        self.warna = "merah"

mobil_1 = Mobil()
mobil_2 = Mobil()

print(mobil_1.warna)
print(mobil_2.warna)

#mengubah atribut instance
mobil_1.warna = "hitam" #atribut kelas

#menampilkan kembali atribut warna
print(mobil_1.warna)
print(mobil_2.warna)

print("-------------")

class Mobil:
    def __init__(self,warna,merek,kecepatan):
        self.warna = warna
        self.merek = merek
        self.kecepatan = kecepatan

mobil_1 = Mobil('merah','lambo',160)

print(mobil_1.warna)
print(mobil_1.merek)
print(mobil_1.kecepatan)

'''Method
method sebagai perilaku atau tindakan yang dapat dilakukan oleh objek atau kelas. 
Pada pembuatan metode , sebenarnya kita membuat fungsi di dalam kelas itu sendiri. 
Dengan kata lain, kita menggunakan kata kunci "def" atau membuat fungsi sebagai suatu metode.'''

print("________________")
print("DECORATOR")
print("________________")

def my_decorator(func):
    def wrapper():
        print("sebelum fungsi dieksekusi")
        func()
        print("setelah fungsi dieksekusi")
    return wrapper

#dekorasi fungsi dengan dekorator
@my_decorator
def say_hello():
    print("hello world!")

#memanggil fungsi yang sudah di dekorasi
say_hello()

'''
secara alur, ketika fungsi say_hello() dipanggil, 
sebenarnya yang dieksekusi adalah fungsi wrapper() yang menjadi hasil dari dekorasi. 
Oleh karena itu, pesan "Sebelum fungsi dieksekusi." dicetak terlebih dahulu, 
kemudian fungsi say_hello() dieksekusi dan mencetak "Hello, world!", 
lalu akhirnya, pesan "Setelah fungsi dieksekusi." dicetak.
'''

print("________________")
print("METODE DARI OBJEK")
print("________________")

class Mobil:
    def __init__(self,warna,merek,kecepatan):
        self.warna = warna
        self.merek = merek
        self.kecepatan = kecepatan

    def tambah_kecepatan(self):
        self.kecepatan += 10

mobil_1 = Mobil("merah","lambo",160)
print("sebelum ditambahkan: ")
print(mobil_1.kecepatan)

mobil_1.tambah_kecepatan() #memanggil metode tambah_kecepatan

print("setelah ditambah kecepatan: ")
print(mobil_1.kecepatan)

'''
Static method adalah fungsi atau method pada sebuah kelas yang bersifat 
statis. Artinya, metode atau fungsi ini bersifat independen dan tidak terikat 
pada instance kelas. Metode ini dapat dianggap seperti kita membuat fungsi
seperti biasa, tetapi didefinisikan dalam kelas sehingga ini menjadi perilaku 
untuk kelas tersebut.Untuk membuat static method, Anda bisa menambahkan 
dekorator @staticmethod tepat sebelum mendefinisikan fungsi atau metode.
'''
print("________________")
print("METODE SECARA STATIS")
print("________________")

class Mobil:
    def __init__(self,merek):
        self.merek = merek

    @staticmethod
    def intro_mobil():
        print("ini adalah metode dari kelas mobill")

Mobil.intro_mobil()
mobil_1 = Mobil("lambo")
mobil_1.intro_mobil()

'''Pada contoh di atas, kita membuat sebuah fungsi bernama intro_mobil() yang 
menjadi metode atau perilaku dari kelas Mobil dengan diawali oleh dekorator 
@staticmethod. Fungsi atau metode yang kita buat bernama intro_mobil dan 
mencetak pesan "ini adalah metode dari kelas Mobil".'''

print("________________")
print("METODE KELAS")
print("________________")

class Mobil:
    def __init__(self,merek):
        self.merek = merek

    @classmethod
    def intro_mobil(cls):
        print("ini adalah metode dari kelas mobil")

Mobil.intro_mobil()
mobil_1 = Mobil("lambo")
mobil_1.intro_mobil()

print("________________")
print("CONTOH METODE KELAS")
print("________________")

class Mobil:
    def __init__(self, merek):
        self.merek = merek

    @classmethod
    def intro_mobil(*args):
        print(args)
        
Mobil.intro_mobil()
mobil_1 = Mobil("DicodingCar")
mobil_1.intro_mobil()

'''
Perhatikan lebih baik output-nya, kode di atas menerima sebuah 
parameter, yakni kelas Mobil walaupun ketika pemanggilan fungsi 
intro_mobil() kita tidak memberikan argumen apa pun.
'''

print("________________")
print("INHERITANCE/PEWARISAN")
print("________________")

class Mobil:
    def __init__(self,warna,merek,kecepatan):
        self.warna = warna
        self.merek = merek
        self.kecepatan = kecepatan

    def tambah_kecepatan(self):
        self.kecepatan +=10

mobil_1 = Mobil("merah","lambo",160)
print(mobil_1.kecepatan)

class MobilSport(Mobil):
    def turbo(self):
        self.kecepatan += 50

#kelas mobil dasar
mobil_1 = Mobil("merah","lambo",160)
print(mobil_1.kecepatan)

#kelas mobil sport
mobil_sport_1 = MobilSport("hitam","avanza",160)
print(mobil_sport_1.kecepatan)
mobil_sport_1.turbo()
print(mobil_sport_1.kecepatan)

print("________________")
print("OVERRIDE")
print("________________")

class Mobil:
    def __init__(self, warna,merek,kecepatan):
        self.warna = warna
        self.merek = merek
        self.kecepatan = kecepatan
    
    def tambah_kecepatan(self): #tambah kecepatan
        self.kecepatan += 10

class MobilSport(Mobil):
    def turbo(self):
        self.kecepatan += 50

    def tambah_kecepatan(self): #tambah kecepatan
        self.kecepatan += 20 

#kelas mobil sport
mobil_sport_1 = MobilSport("hitam","avanza",160)
print(mobil_sport_1.kecepatan)
mobil_sport_1.tambah_kecepatan() #memanggil metode baru menambah kecepatan
print(mobil_sport_1.kecepatan)

'''
Namun, perlu dipahami bahwa menimpa bukan berarti mengubah metode 
dari kelas induk. Hal ini karena metode dari kelas baru tersebut merupakan 
hasil dari pewarisan sehingga tidak akan mengubah metode dari kelas induk.
'''
print("________________")
print("SUPER CLASS")
print("________________")

class Mobil:
    def __init__(self,warna,merek,kecepatan):
        self.warna = warna
        self.merek = merek
        self.kecepatan = kecepatan

    def tambah_kecepatan(self):
        self.kecepatan += 10

class MobilSport(Mobil):
    def turbo(self):
        self.kecepatan += 50

    def tambah_kecepatan(self):
        super().tambah_kecepatan()
        print("kecepatan anda meningkat hati hati")

#kelas mobil sport
mobil_sport_1 = MobilSport("hitam","avanza",160)
mobil_sport_1.tambah_kecepatan()
print(mobil_sport_1.kecepatan)

'''
Pada metode ini, kita menggunakan "super()" untuk mengambil metode 
tambah_kecepatan yang berasal dari super class atau induknya, yaitu kelas 
Mobil. Dengan begitu, program akan menjalankan metode tersebut dan di 
bawahnya kita menambahkan teks baru sesuai kebutuhan pada kelas turunan 
berupa "Kecepatan Anda meningkat! Hati-hati!".
'''

print("________________")
print("KUIS DICODING")
print("________________")


class Animal:
    def __init__(self,name,age,species):
        self.name = name
        self.age = age
        self.species = species

class Cat(Animal):
    def deskripsi(self):
        return f"{self.name} adalah kucing berjenis {self.species} yang sudah berumur {self.age}tahun"
    
    def suara(self):
        return "meow"
    
#membuat instance dari class cat    
MyCat = Cat("Neko",3,"Persian")
#menampilkan deskripsi dan suara mycat   
print(MyCat.deskripsi())
print(MyCat.suara())


print("versi gpt")

class Animal:
    def __init__(self, name, age, species):
        self.name = name
        self.age = age
        self.species = species

class Cat(Animal):
    def deskripsi(self):
        return f"{self.name} adalah kucing berjenis {self.species} yang sudah berumur {self.age} tahun"
    
    def suara(self):
        return "meow!"

# Membuat instance dari kelas Cat
myCat = Cat(name="Neko", age=3, species="Persian")

# Contoh penggunaan
print(myCat.deskripsi())  # Output: Neko adalah kucing berjenis Persian yang sudah berumur 3 tahun
print(myCat.suara())      # Output: meow!

print("________________")
print("KUIS DICODING")
print("________________")

class Mobil:
    def __init__(self):
    self.warna = "merah"