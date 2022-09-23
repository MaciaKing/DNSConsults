import dns

class DNS:
   def __init__(self, dnsIPs, domain):
      self.domain=domain #List of domains consulting
      self.dnsIPs=dnsIPs #List of DNS ips

   def consultDomain(self):
      print(" DOMAIN = ", self.domain)
   
   def viewDNSIps(self):
      print(" MY DNS = ", self.dnsIPs)
