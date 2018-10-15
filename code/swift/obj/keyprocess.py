
import os
import string
import random
from DB import Conn
config = {
    'host': '127.0.0.1',
    'port': 3306,
    'user': 'root',
    'passwd': 'adc',
    'db': 'keyencry',
    'charset': 'utf8'
    }
class keygenerate(object):
    keytext=b''
    def __init__(self,info):
        conn=Conn(config)
        is_exist=conn.is_keyexist(info)#if the key is already in db
        if (is_exist==True):
            co=conn.fetch_job(info)
            self.keytext=co
        else:
            ran_str = ''.join(random.sample(string.ascii_letters + string.digits, 32))
            info['key']=ran_str
            self.keytext=bytes(ran_str.encode('utf8'))#for python2.x
            co=conn.insert_job(info)
    def __call__(self):
        return self.keytext

class keyfetch(object):
    keytext=b''
    def __init__(self,info):
        conn=Conn(config)
        co1=conn.fetch_job(info)
        self.keytext=co1
    def __call__(self):
        return self.keytext
        
