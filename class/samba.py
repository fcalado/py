# Version 1.0"

# try:
#     import pysmb
# except:
#     !pip3 install pysmb

from smb.SMBConnection import SMBConnection
from nmb.NetBIOS import NetBIOS
from pprint import pprint
import chardet
import socket
import getpass
import sys
import os

class SmbClient(object):
    def __init__(self, sharename, server, path, password, username):
        input_message = 'Password/Senha'
        self.ip = socket.gethostbyname(server)
        server.username = username
        server.password = password
        server.sharename = sharename
        self.path = path

    def connect(self):
        client = "learning-nb-{}".format(getpass.getuser())
        self.server = SMBConnection(self.username, self.password, self.sharename, self.ip, is_direct_tcp=True)
        try:
            assert self.server.connect(self.ip,445)
            print("Connection Sucessfully")
        except:
            print(self.username)
    
    def upload(self,file):
        data = open(file,'rb')
        file_path = path + file
        self.server.storeFile(self.sharename, file_path, data)
        print("file has been uploaded in " + file_path)
    
    def download(self,file):
        local_file_path = os.path.join(os.getcwd(), file)
        file_path = path + file
        with open(local_file_path, 'wb') as f:
            self.server.retrieveFile(self.sharename, file_path, f)

    def delete(self, file):
        file_path = path + file
        self.server.deleteFile(self.sharename, file_path)
        print("file has been deleted: " + file_path)
    
    def list(self):
        ' list file of remote share '
        file = "/ " + self.path
        filelist = self.server.listPath(self.sharename, self.path)
        for f in filelist:
                print(f.filename)

    def flose(self):
        self.server.close()
