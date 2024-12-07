import numpy as np

arr3 = np.array([[1, 2, 3, 4], [5, 6, 7, 8], [9, 10, 11, 12]])
newarr3 = arr3[:2 ,1:3]

newarr3[0,0] =22

print(arr3)
