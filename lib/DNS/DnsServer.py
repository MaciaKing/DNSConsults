import dns
import dns.resolver

class DNS:
   def __init__(self, dnsIPs):
      self.dnsIPs=dnsIPs #List of DNS ips     
      self.res=dns.resolver.Resolver(configure=False)
      self.dicc={}
   
   def viewDNSIps(self):
      print(" MY DNS = ", self.dnsIPs)


   def getIp(self, domainToConsult):
      """
      De dominio --> a IP
      """
      self.dicc={} #Reset dicc
      for i in  self.dnsIPs:
        self.res.nameservers=[i]
        try:
          r=self.res.query(domainToConsult, 'a', tcp=True)
          for rdata in r:
            if rdata.to_text() in self.dicc:
              self.dicc[rdata.to_text()]=self.dicc[rdata.to_text()]+1
            else:
              self.dicc[rdata.to_text()]=1
        except:        
          print(" --> DNS(",i,") can not resolve this IP")

      self.printDicc()
      return self.dicc
         
   def getDomain(self, domainToConsult):
      """
      De dominio --> a servidores DNS
      """
      for i in  self.dnsIPs:
        try:
          r=self.res.resolve(domainToConsult,'A')
          nameservers = [ns.to_text() for ns in r]
          print(nameservers)
        except:        
          print(" --> DNS(",i,") can not resolve this Domain")
   
   
   def printDicc(self): 
      """
      Muestra nuestro diccionario
      """
     dictionary_items = self.dicc.items()
     for item in dictionary_items:
       print(item)
   