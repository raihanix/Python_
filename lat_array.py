# x = [1, 2, 3, 4, 5]
# print(x)

# #array
# import array

# x= array.array("i",[1,2,3,4,5]) #i di dalam itu berarti interger
# print(x)
# print(type(x))

# nama_siswa1 = 90
# nama_siswa2 = 100
# nama_siswa3 = 50
# nama_siswa4 = 80
# nama_siswa5 = 85
# nama_siswa6 = 45
# nama_siswa7 = 80
# nama_siswa8 = 75
# nama_siswa9 = 50
# nama_siswa10 = 60

# print(nama_siswa1)
# print(nama_siswa2)
# print(nama_siswa3)
# print(nama_siswa4)
# print(nama_siswa5)
# print(nama_siswa6)
# print(nama_siswa7)
# print(nama_siswa8)
# print(nama_siswa9)
# print(nama_siswa10)

# siswa = [90,100,50,80,85,45,80,75,50,60]
# print(siswa)
# print(siswa[0])

# var_list = [1,2,3]
# for elemen in var_list:
#     print(id(elemen))

# var_arr = [9,8,6,5,4,3,2,1,0]
# print(var_arr)

# var_arr = [0 for i in range(10)]
# print(var_arr)

# var_arr = [0 for i in range(10)]
# for i in range(10):
#     var_arr[i] = i

# print(var_arr)

# var_arr = [1,2,3,4,5]

# for i in range(len(var_arr)):
#     current_element = var_arr[i]
#     next_index = i+1

#     if next_index < len(var_arr): #len berfungsi untuk menghitung panjang 
#         next_element = var_arr[next_index]

#     else:
#         next_element = None
    
#     print(f"current element: {current_element}, next_element:,{next_element}")

# var_arr = [1,7,2,89,3]
# left_pointer = var_arr[0]

# for i in range(1, len(var_arr)):
#     right_pointer = var_arr[i]
#     if right_pointer > left_pointer:
#         left_pointer = right_pointer

# print(left_pointer)

# Array yang diberikan
var_array = [i for i in range(101)]

# Inisialisasi variabel untuk penjumlahan dan rata-rata
total = 0
result = 0

# Melakukan perulangan untuk menjumlahkan elemen array
for element in var_array:
    total += element

# Menghitung rata-rata dengan membagi total dengan jumlah elemen
result = total / len(var_array)

# Menampilkan hasil
print(f"Rata-rata dari array: {result}")
