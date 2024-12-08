import numpy as np

b = np.array([[1,2,3,4],[5,6,7,8],[9,10,11,12],[13,14,15,16]])

boolb = (b%3 == 0)
c = np.array([[0,0,0,0],[0,0,0,0],[0,0,0,0],[0,0,0,0]])
i = 0
for i in range(4):
    j=0
    for j in range(4):
        if boolb[i,j] == True:
            c[i,j] = np.array([b[i,j]])

print(c)