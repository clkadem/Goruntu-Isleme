import os
import numpy as np
import matplotlib.pyplot as plt

def get_jpeg_files():
    print(os.getcwd())
    print(os.listdir())
    path = os.getcwd()
    jpg_files = [f for f in os.listdir(path) if f.endswith('.jpg')]
    return jpg_files

def compare_list_ndarray():

    # https://docs.pythpn.org/3/library/ctypes.html
    # numpy as np
     list1 = [1,'dafasfasgaaf',2,3,4] #broadcast
     list2 = [1,2,'gsdfsg',35,455] #broadcast
     print(list1+list2) #+

     list5 = [1,2,3,4] #broadcast
     list6 = [1,2,3,4] #[1,2,'gsdfsg',35,455] broadcast
     print(list5+list6+[10]) #+list5 + list6 + 10 error

     list3 = np.asarray([1,2,3,4])  #ndarray asattay
     list4 = np.asarray([1,2,3,4])
     print(list3+list4+10)

get_jpeg_files()
image_1 = plt.imread('pic_1.jpg')
print(type(image_1),image_1.ndim)
m,n,k = image_1.shape
for i in range(10):
    for j in range(10):
        temp_1 = image_1[i,j]
        print(temp_1[2],end=" ")         # R G B

image_2 = image_1 + 10
print()
print(image_1.shape,image_2.shape)
print(image_1[25,299,:],image_2[25,299,:])



def my_display_two_image(im_1,im_2):

    plt.subplot(1, 2, 1)
    plt.imshow(im_1)

    plt.subplot(1, 2, 2)
    plt.imshow(im_2)

    plt.show()

def rotate(im_1):
    m,n,k = im_1.shape
    new_image = np.zeros((n,m,k), dtype='uint8')
    for i in range(m):
        for j in range(n):
            temp = im_1[i, j]
            new_image[j, i] = temp
    return new_image
my_display_two_image(image_1,image_2)
image_3 = rotate(image_1)
my_display_two_image(image_1,image_3)