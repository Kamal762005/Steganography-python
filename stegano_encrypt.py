import cv2
import string

def encrypt(input_text,c,d,p):
    path=input("Enter Path Of Image To Encrypt: ")
    path = path.replace("\"",'')
    img1 = cv2.imread(path)

    #img1="/img1.jpg"
    # storing password into an image
    n,m=img1.shape[:2]
    z=0
    for i in range(len(p)):
        img1[n-1,m-1,z] = d[p[i]]
        n = n - 1
        m = m - 1
        z = (z + 1) % 3
    
    # storing data into an image
    m, n, z = 0, 0, 0
    for i in range(len(input_text)):
        img1[n,m,z] = d[input_text[i]]
        n = n + 1
        m = m + 1
        z = (z + 1) % 3
    img1 = cv2.imwrite("encrypted_image.png",img1)
    return img1
