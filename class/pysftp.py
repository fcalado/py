# Version 1.0

# try:
#     import pysftp
# except:
#     !pip3 install pysftp

from nmb.NetBIOS import NetBIOS
from pprint import pprint
import chardet
import socket
import getpass
import sys
import pysftp

cnopts = pysftp.CnOpts()
cnopts.hostkeys = None

class PysftpClient(object):
        def __init__(self, myUsername, myPassword, remoteHostname, remoteFilePath, localFilePath):
                self.myUsername = myUsername
                self.myPassword = myPassword
                self.remoteHostname = remoteHostname
                self.remoteFilePath = remoteFilePath
                self.localFilePath = localFilePath
        
        def colletionTest(self):
                try:
                        with pysftp.Connection(host=self.remoteHostname, username=self.myUsername, password=self.myPassword, cnopts=cnopts) as sftp:
                                print("Connection Sucessfully")
                except:
                        print("One parameter could be wrong, parameter used -> User: " + self.myUsername +
                              " Password: " + self.myPassword + 
                              " Server: " + self.remoteHostname + 
                              " Remote Server: " + self.remoteFilePath + 
                              " Local File Path: " + self.localFilePath)
        
        def getSingleFile(self,file):
                try:
                        with pysftp.Connection(host=self.remoteHostname, username=self.myUsername, password=self.myPassword,cnopts=cnopts) as sftp:
                                sftp.chdir(file, self.remoteFilePath)
                                sftp.get(file)
                except:
                        with pysftp.Connection(host=self.remoteHostname, username=self.myUsername, password=self.myPassword,cnopts=cnopts) as sftp:
                                print("File not found")

        def uploadSingleFile(self,file):
                try:
                        with pysftp.Connection(host=self.remoteHostname, username=self.myUsername, password=self.myPassword,cnopts=cnopts) as sftp:
                                sftp.chdir(self.remoteFilePath)
                                sftp.put(file, preserve_mtime=True)
                except:
                        with pysftp.Connection(host=self.remoteHostname, username=self.myUsername, password=self.myPassword,cnopts=cnopts) as sftp:
                                print("File not found")
        
        def getAllFilesFromDirectory(self):
                try:
                        with pysftp.Connection(host=self.remoteHostname, username=self.myUsername, password=self.myPassword,cnopts=cnopts) as sftp:
                                sftp.get_d(self.remoteFilePath, self.localFilePath)
                                #fetch all files
                                # for file_name in sftp.listdir(self.remoteFilePath):
                                #         destination = self.remoteFilePath + "/" + file_name
                                #         if sftp.isfile(destination):
                                #                 sftp.remove(destination)
                                #                 print("Deleted: ", file_name)
                except:
                        print("Can't possbile move the file " + self.remoteFilePath + " for the directory " + self.localFilePath)