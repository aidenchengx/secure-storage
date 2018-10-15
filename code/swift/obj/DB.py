'''
Created on 2018.8.20

@author: cx597swift
'''
from MySQLdb import Connection


class Conn(object):
    '''
    classdocs
    '''
    def __init__(self, config):
        '''
        Constructor
        '''
        self.config=config
        conn=Connection(**config)
        if not conn:
            #print("connection failed")
            pass
        self.cursor=conn.cursor()
        self.conn=conn
    def fetch_job(self,info):
        command='select keytext from keytable where group_type="'+info['type']+'" and group_token="'+info['token']+'";'
        self.cursor.execute(command)
        re=self.cursor.fetchone()
        if not re:
            print("given token not exist")
        else:
            self.conn.close()
            self.cursor.close()
            str1=re[0]
            str1=bytes(str1.encode('utf8'))
            return str1
    def insert_job(self,info):
        none='none'
        command='insert into keytable values("%s","%s","%s");'%(info['type'],info['token'],info['key'])
        self.cursor.execute(command)
        #self.cursor.execute("")
        self.cursor.close()
        self.conn.commit()
        self.conn.close()
    def is_keyexist(self,info):
        command='select keytext from keytable where group_type="%s" and group_token="%s";'%(info['type'],info['token'])
        self.cursor.execute(command)
        count=self.cursor.rowcount
        if count>0:
            #print("key exist already")
            return True        
        pass
        
