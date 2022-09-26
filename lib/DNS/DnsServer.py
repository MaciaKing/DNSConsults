import dns
import dns.resolver

#https://programmerclick.com/article/8131998611/
class DNS:
   def __init__(self, dnsIPs):
     # self.domain=domain #Domain to consult
      self.dnsIPs=dnsIPs #List of DNS ips     
      dns.resolver.default_resolver = dns.resolver.Resolver(configure=False)
      dns.resolver.default_resolver.nameservers = self.dnsIPs

   def consultDomain(self):
      print(" DOMAIN = ", self.domain)
   
   def viewDNSIps(self):
      print(" MY DNS = ", self.dnsIPs)

   def doConsult(self, domainToConsult):
      print("DNS server--> "+self.dnsIPs[0])
      r=dns.resolver.query(domainToConsult, 'a', tcp=True)
      for rdata in r:
         print( "IP --> ", rdata.to_text())
