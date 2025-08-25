from Crypto.Cipher import AES
from Crypto.Util.Padding import pad, unpad
from Crypto.Random import get_random_bytes
import base64

# pt - plain text
# ect - encoded cipher text
# iv - initialization vector
# ctb - cipher text bytes
# 

# Function to encrypt
def aes_encrypt(pt, key):
    # Convert key to 16, 24, or 32 bytes (AES requirement)
    key = key.encode('utf-8')
    key = pad(key, AES.block_size)  # Ensure key is 16/24/32 bytes

    iv = get_random_bytes(AES.block_size)  # Initialization vector
    cipher = AES.new(key, AES.MODE_CBC, iv)
    
    ctb = cipher.encrypt(pad(pt.encode('utf-8'), AES.block_size))
    
    # Combine iv and ciphertext and encode in base64 for storage
    return base64.b64encode(iv + ctb).decode('utf-8')

# Function to decrypt
def aes_decrypt(ect, key):
    key = key.encode('utf-8')
    key = pad(key, AES.block_size)

    raw = base64.b64decode(ect)
    iv = raw[:AES.block_size]
    ciphertext = raw[AES.block_size:]

    cipher = AES.new(key, AES.MODE_CBC, iv)
    pt = unpad(cipher.decrypt(ciphertext), AES.block_size)
    return pt.decode('utf-8')


