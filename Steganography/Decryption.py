# import required libraries and packages
from cryptography.fernet import Fernet as fn
from PIL import Image
from steganography import *
import os

class Decryption:
    def load_data(self):
        ''' This function loads data from the file and returns it.
            The value returned is a list storing line by line data of the file.
        '''
        
        data = open("private.key").readlines()
        return data

    def decrypt(self):
        ''' this function decrypts the message and returns the original message.
        '''
        
        data = self.load_data() #loading the data in a variable
        
        key = data[0]# reading the key from the recieved data
        f = fn(key) # passing to fernet for recognition
        
        image = Image.open(data[4])
        enc_msg = decode(image)

        enc_msg = enc_msg.replace("b'", '')
        enc_msg = enc_msg.replace("'", '')
        
        # passing the encrypted message and converting it to bytes from string
        decrypted_msg = f.decrypt(bytes(enc_msg, 'UTF-8'))

        msg = decrypted_msg.decode()  # removing the second layer encryption i.e. basic decoding

        return msg
