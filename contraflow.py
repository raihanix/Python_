# ready = "daging ayam"

# if ready == "daging ayam":
#     print("ibu membeli dan memasak ayam")
# else:
#     print("ibu membeli dan memasak tempe")

# score = 100
# if score == 100:
#     print("mantap euy 100")

# x=''
# if x:
#     print("ini True")

# tinggi = 120
# if tinggi <= 160:
#     print("tidak boleh menaiki orang")
# else:
#     print("boleh menaiki orang")

# nilai = 65

# if nilai >=80:
#     print('selamat kamu mmendapat nilai A')
# elif nilai >=75:
#     print("selamat kamu mendapat nilai B")
# else:
#     print("Kamu dapat nilai C, coba lagi")

# nilai = 81
# perilaku = "tidak baik"

# if nilai>=80 and perilaku == "baik":
#     print("selamat kamu bagus")
# elif nilai>=80 and perilaku != "baik":
#     print("nilai kamu bagus cuman kamu nakal")
# else:
#     print("udah bodoh nakal lagi")

# lulus = True #ternary operators (hasil+kondisi+salah)
# # print("selamat!") if lulus else print("goblok!")

# if lulus:
#     print("selamat")
# else:
#     print("perbaiki!")

# #ternary tuples (salah+benar+kondisi)
# lulus = True
# kelulusan = ("perbaiki anda belum lulus!","selamat anda lulus")[lulus]
# print(kelulusan)

# #iterable perulangan
# var_list = [1,2,3,4,5,6,7,8,9,10]
# for i in var_list:
#     print(i)

# for i in range(10):
#     print(i+1)

# #perulangan menggunakan start,stop,step
# for i in range(1,10,2):
#     print(i)

# #while
# counter = 1
# while counter <= 5:
#     print(counter)
#     counter +=1 #increment

# #nested loop
# for i in range(1,3):
#     for j in range(1,3):
#         print(1,j)

# #break
# for i in range(2):
#     print("perulangan luar")
#     for j in range(10):
#         print("perulangan dalam")
#         if j==1:
#             break #menghentikan perulangan dalam jika j=i

# for huruf in 'dico ding':
#     if huruf == ' ':
#         break
#     print('huruf saat ini:{}'.format(huruf))

# for huruf in 'dico ding':
#     if huruf == ' ':
#         continue
#     print("huruf saat ini:{}".format(huruf))

# #else setelah for
# number = [1,2,3,4,5]
# for num in number:
#     if num==6:
#         print("angka ditemukan,berhenti!")
#         break
# else:
#     print('angka tidak ditemukan')

# #else setelah while
# count = 0
# while count < 3:
#     print("rehan")
#     count +=1
# else:
#     print("blok else dieksekusi karena while salah")

# n = 10
# while n > 0:
#     n = n - 1
#     if n == 7:
#         break
#     print(n)
# else:
#     print("loop selesai")

# #pass (karena jika kondisi terpenuhi, program tidak akan melakukan apa pun)
# x = 10 
# if x > 5:
#     pass
# else:
#     print("nilai tidak memenuhi kondisi")

# #list comprehension
# angka = [1,2,3,4]
# pangkat = []
# for n in angka:
#     pangkat.append(n**2)
# print(pangkat)

# angka = [1,2,3,4]
# pangkat = [n**2 for n in angka]
# print(pangkat)

# evenNumber = [i for i in range(0,501,2)]
# print(evenNumber)

# #penanganan kesalahan
# z=0
# try:
#     print(1/z)
# except ZeroDivisionError:
#     print("eror kan kata gue teh")

# var_dict = {"rata_rata":"1.0"}

# try:
#     print(f"rata rata adalah {var_dict['rata rata']}")
# except KeyError:
#     print("key tidak ditemukan")
# except TypeError:
#     print("gabisa dibagi string")
# else:
#     print("kode ini deksekusi jika idak ada exception")
# finally:
#     print("kode ini dieksekusi dari ada atau tidak adanya exception")

var = -1
if var < 0:
    raise ValueError("bilangan gaada monyet")
else:
    for i in range(var):
        print(i+1)