'''
Created on 2018.8.13

@author: cx597
'''

import sys
import os
from cryptography.hazmat.primitives.ciphers import Cipher,algorithms,modes
#from email.policy import default
from cryptography.hazmat.backends import default_backend

class Crypto(object):
    cipher='AES_CTR_256'
    key_length=32
    iv_length=int(algorithms.AES.block_size/8)
    
    
    def __init__(self,key,iv):
        self.backend=default_backend()
        if len(key)==32: 
            self.key=key
        else:
            self.key=self.create_random_key()
        if len(iv)==16:
            self.iv=iv
        else: 
            self.iv=self.create_iv()
        
    def __call__(self):
        pass
        
    def create_encryption_ctxt(self):
        engine=Cipher(algorithms.AES(self.key),modes.CTR(self.iv),self.backend)
        return engine.encryptor()
    
    def create_iv(self):
        return os.urandom(self.iv_length)
    
    def create_random_key(self):
        return os.urandom(self.key_length)

    def create_decryption_ctxt(self):
        engine=Cipher(algorithms.AES(self.key),modes.CTR(self.iv),self.backend)
        return engine.decryptor()
            
