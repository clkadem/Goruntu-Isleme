#DERS1

import numpy as np
import matplotlib.pyplot as plt

list_1=[1,'2',3,4,5]

image_1=plt.imread('pic_1.jpg')
#x y
# pixel , 400x600 resolution , dpi

print(type(image_1))

a = image_1.shape
print(a)
for row in range(5):
    for col in range(5):
        print(image_1[row,col,0],image_1[row,col,1],image_1[row,col,2])  #RGB ,pixel ,intensity


plt.imshow(image_1)
plt.show()

