import os
import readline
from lib.ReadWriteFile.ReadFile import ReadFile

PATHdnsIPS= "/lib/DNS/dnsIp.txt"

def showDnsIP():
    rf= ReadFile(os. getcwd()+PATHdnsIPS) #Move to correct pwd
    rf.openFile()
    line=rf.readLine()
    while line != "":
        print(line)
        line=rf.readLine()

if __name__ == "__main__":
    
    showDnsIP()
    #dns = DNS("google.com")
    
    #dns.consultDomain()