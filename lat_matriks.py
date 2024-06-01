# matriks = [[1, 2, 3],
#           [4, 5, 6],
#           [7, 8, 9]]
            
# print(matriks)

# import numpy

# matriks = numpy.array([[1, 2, 3], [4, 5, 6], [7, 8 ,9]])
# print(matriks)


# import numpy
# import sys

# var_list= [[1,2,3],[4,5,6],[7,8,9]]
# var_array= numpy.array([[1,2,3],[4,5,6],[7,8,9]])
# print("ukuran keseluruhan elemen list dalam bytes = ",sys.getsizeof(var_list)*len(var_list))
# print("ukuran keseluruhan elemen numpy dalam bytes = ",var_array.size*var_array.itemsize)

# matriks = numpy.array([[1,0,0,0,0],
#            [0,1,0,0,0],
#            [0,0,1,0,0],
#            [0,0,0,1,0],
#            [0,0,0,0,1]])

# print(matriks)

# var_mat = [[1, 2, 3, 4, 5], #baris ke 0
#            [6, 7, 8, 9, 10], #baris ke 1
#            [11, 12, 13, 14, 15], #baris ke 2
#            [16, 17, 18, 19, 20], #baris ke 3
#            [21, 22, 23, 24, 25]] #baris ke 4
           
# print(var_mat[2][1]) #baris ke-2 kolom ke 1

#membuat matriks 2x2
var_mat =[[5,0],
          [1,-2]]
def_mat = [[0 for j in range(2)] for i in range(2)]

for i in range(len(var_mat)):
    for j in range(len(var_mat[0])):
        def_mat[i][j] = var_mat[i][j]*2
print(def_mat)

import numpy as np 

var_mat = np.array([[5,0],
                    [1,-2]])
result = var_mat*2
print(result)