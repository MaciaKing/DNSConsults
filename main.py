import os
import sys # Para los argumentos
from lib.ReadWriteFile.ReadFile import ReadFile
from lib.DNS.DnsServer import DNS

#GLOBAL VARS
PATHdnsIPS= "/lib/DNS/dnsIp.txt" # All IPs from DNS
DNSIP=[] # All IPs of DNS
dns=None # Object DNS

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
  rf.closeFile()


def loadDns():
  global dns
  loadDnsIP()
  dns=DNS(DNSIP)
  
def raiseError(s):
  menu()
  raise("Error: ", s)


def menu():
  None


### MAIN ###
if __name__ == "__main__":
  if len(sys.argv)>=2:
    if sys.argv[1]== 'd':
      print("DOMAIN ",sys.argv[2])
      loadDns()
      dns.getIp(sys.argv[2])
    elif sys.argv[1]== 'i':
      print("IP ",sys.argv[2])
      loadDns()
      dns.getDomain(sys.argv[2])
    else:
      raiseError("LOS PARAMETROS DE ENTRADA NO SON CORRECTOS")
          
  else:        
    raiseError("Faltan argumentos")
