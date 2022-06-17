#import necessary libraries and packages
from cryptography.fernet import Fernet as fn
from steganography import *
from PIL import Image
import random
import os

def generate_key():
    ''' this function creates a unique key for particular encryption and
        writes it to a file.
    '''
    key = fn.generate_key()  #generatekey using fernet.

    with open("private.key", "wb") as key_file:
        #writing key to the file
        key_file.write(key)

def load_key():
    ''' This function loads the key from the file and retuens the value.
    '''
    generate_key()
    return open("private.key", "rb").read()

def encrypt(msg):
    ''' This function is for encrypting the message and binding it with
        the key generated and saving the encrypted message to a text file
        along with the key.
    '''
    key = load_key() #loading the key from file
    encoded_msg = msg.encode() #Encoding a message i.e. single layer encryption

    f = fn(key)  #passing the key to fernet for binding it with encryption
    #double encryption to the message using fernet
    encrypted_msg = f.encrypt(encoded_msg)

    path = ".\\Images"
    images = os.listdir(path)
    image = random.choice(images)

    image = Image.open("Images" + "/" + image)

    newimg = image.copy()
    w = newimg.size[0]
    (x, y) = (0, 0)
    
    for pixel in modPix(newimg.getdata(), encrypted_msg):
        newimg.putpixel((x, y), pixel)
        if (x == w - 1):
            x = 0
            y = y + 1
        else:
            x = x + 1

    new_names = ['encrypted.png', 'done.png', 'okay.png']
    new_name = random.choice(new_names)
    newimg.save(new_name)

    with open("private.key", "a") as enc_file:
        enc_file.write("\n \n \n \n")
        enc_file.write(new_name)
