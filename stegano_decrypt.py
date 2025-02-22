import cv2
import string

def decrypt(c,d):
    path=input("Enter Path Of Image To Decrypt: ")
    path = path.replace("\"",'')
    img1 = cv2.imread(path)

    #img1="/img1.jpg"
    # Retriving the password from the image.
    password = ""
    n , m = img1.shape[:2]
    z = 0
    for i in range(255):
        if(c[img1[n-1,m-1,z]]=='!'):
            break
        password=password + c[img1[n-1,m-1,z]]
        n = n - 1
        m = m - 1
        z = (z + 1) % 3
    
    # Retriving the data from the image.
    password1 = input("Enter Password For Decryption: ")
    if (password1 == password):
        msg = ""
        m, n, z = 0, 0, 0
        for i in range(255):
            if(c[img1[n,m,z]]=='$'):
                break
            msg=msg + c[img1[n,m,z]]
            n = n + 1
            m = m + 1
            z = (z + 1) % 3
        print("Decrypted message: ",msg)
    else:
        print("YOU ARE NOT AUTHENTICATED!")
