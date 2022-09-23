#from ReadWriteFile import ReadFile
#from ..ReadWriteFile.ReadFile import ReadFile
import dns

class DNS:
   def __init__(self, domain):
      self.domain=domain
      self.IPList=[]

   def consultDomain(self):
      print("self.domain= ", self.domain)

   def showIpDNS(self):
      None