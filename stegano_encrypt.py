import cv2
import string
import AES 

def encrypt(input_text,c,d,p):
    path=input("Enter Path Of Image To Encrypt: ")
    path = path.replace("\"",'')
    img1 = cv2.imread(path)

    # calculating height and width.
    h,w=img1.shape[:2]
    
    # using aes algorithm, we can encrypt text and embedded into a image.
    # $ - indicates end of cipher text.
    ct = AES.aes_encrypt(input_text,p)+'$'
    
    # check for maximum capacity of an image to store the text.
    max=h*w*3
    if len(ct) > max:
        print("Error: Input text is too long for the selected image.")

    # storing data into an image using 3 channels(3 characters are stored in a single pixel).
    v = 0
    for i in range(h):
        for j in range(w):
            for k in range(3):
                if v < len(ct):
                    img1[i, j, k]=d[ct[v]]
                    v += 1
                else:break
            if(v>len(ct)):break
        if(v>len(ct)):break

    # storing password into an image only using lsb bit of last row.
    # ! - indicates end of password.
    n=h-1
    z=0
    p=p+'!'
    for m in range(min(len(p),w)):
        img1[n,m,z] = d[p[m]]
    img1 = cv2.imwrite("encrypted_image.png",img1)
    return img1
