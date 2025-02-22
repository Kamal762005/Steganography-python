import cv2
import os
import string

# importing the encryption and decryption files

import stegano_encrypt as se
import stegano_decrypt as sd

d, c = {}, {}
for i in range(255):
    d[chr(i)] = i
    c[i] = chr(i)
text = input("Enter Secret Message: ")
password = input("Enter The Password: ")

# "$" indicates the end of the data.
# "!" indicates the end of the password.
img = se.encrypt(text+'$', c, d,password+'!')
os.system("start encrypted_image.png")

sd.decrypt(c,d)
