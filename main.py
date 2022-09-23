import os
from lib.ReadWriteFile.ReadFile import ReadFile
from lib.DNS.DnsServer import DNS

#GLOBAL VARS
PATHdnsIPS= "/lib/DNS/dnsIp.txt" #All IPs from DNS
DNSIP=[] #All IPs of DNS

def loadDnsIP():
    '''
        We load all the IPs of DNS servers on DNSIP. The 
        Ips are on the file "/lib/DNS/dnsIp.txt". 
    '''
    global DNSIP

    rf= ReadFile(os.getcwd()+PATHdnsIPS) #Move to correct pwd
    rf.openFile()
    line=rf.readLine()
    while line != "":
        DNSIP.append(line)
        line=rf.readLine()


if __name__ == "__main__":
    loadDnsIP()
    dns=DNS(DNSIP,"google.com")
    dns.viewDNSIps()
    dns.consultDomain()