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
    Return dicc
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
         
  def getDomain(self, IpToConsult):
    """
    De dominio --> a servidores DNS
    Return a the dicc
    """
    self.dicc={} #Reset dicc
    for i in  self.dnsIPs:
      self.res.nameservers=[i]
      try:
        n = dns.reversename.from_address(IpToConsult)
        print((dns.resolver.query(n,"PTR")[0]).to_text())
        name=(dns.resolver.query(n,"PTR")[0]).to_text()
        if name in self.dicc:
            self.dicc[name]=self.dicc[name]+1
        else:
            self.dicc[name]=1
      except:        
        print(" --> DNS(",i,") can not resolve this IP")
        
    self.printDicc()
    return self.dicc
   
  def printDicc(self): 
    """
    Muestra nuestro diccionario
    """
    dictionary_items = self.dicc.items()
    for item in dictionary_items:
      print(item)
   