import cv2
import string
import AES

def decrypt(c,d):
    path=input("Enter Path Of Image To Decrypt: ")
    path = path.replace("\"",'')
    img1 = cv2.imread(path)
    
    # calculating height and width.
    h,w=img1.shape[:2]
        
    # Retriving the password from the image.
    password = ""
    z = 0
    for col in range(w):
        value = img1[h - 1, col, z]
        if value in c:
            char = c[value]
            if char == '!':
                break
            password += char
        else:
            print(f"Invalid value in password section: {value}")
            return
    
    # Retriving the data from the image.
    password1 = input("Enter Password For Decryption: ")
    if (password1 == password):
        print("YOU ARE AUTHENTICATED.")
        ct = ""
        stop = False
        for i in range(h):
            for j in range(w):
                for k in range(3):
                    value = img1[i, j, k]
                    if value in c:
                        char = c[value]
                        if char == '$':
                            stop = True
                            break
                        ct += char
                if stop:
                    break
            if stop:
                break

        # decrypting the cipher text obtained from image
        msg = AES.aes_decrypt(ct,password)
        print("Decrypted message: ",msg)
    else:
        print("YOU ARE NOT AUTHENTICATED!")

