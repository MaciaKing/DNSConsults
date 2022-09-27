import dns
import dns.resolver

#https://programmerclick.com/article/8131998611/

class DNS:
   def __init__(self, dnsIPs):
      self.dnsIPs=dnsIPs #List of DNS ips     
      #self.res = dns.resolver.Resolver(configure=False)
      self.res=dns.resolver.Resolver(configure=False)
      #self.res.nameservers=self.dnsIPs

   def consultDomain(self):
      print(" DOMAIN = ", self.domain)
   
   def viewDNSIps(self):
      print(" MY DNS = ", self.dnsIPs)

   def doConsult(self, domainToConsult):
      """
      De dominio --> a IP
      """
      for i in  self.dnsIPs:
        self.res.nameservers=[i]
        try:
          r=self.res.query(domainToConsult, 'a', tcp=True)
          #print("RES-->",r)
          for rdata in r:
            print( " --> DNS(",i,")server resolved IP:", rdata.to_text())
          print("\n") #For view output better
        except:        
          print(" --> DNS(",i,") can not resolve this IP")
         

   def doConsult2(self, domainToConsult):
      """
      De dominio --> a servidores DNS
      """
      for i in  self.dnsIPs:
        try:
          r=self.res.resolve(domainToConsult,'NS')
          nameservers = [ns.to_text() for ns in r]
          print(nameservers)
        except:        
          print(" --> DNS(",i,") can not resolve this Domain")
   