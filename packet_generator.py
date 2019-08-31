from scapy.all import *
import oyaml as yaml

f= (open('packet_generator.yaml', 'r')).read()
dict1= yaml.load(f , Loader=yaml.FullLoader)


def geneatingPacket():
  h= []
  for p in dict1:
    for i in dict1[p]:

            for j in dict1[p][i]:
                exec(j)

    for i in dict1[p]:
        if not i == 'Packet' :
            hdr = eval(i)()			# Creating raw headers ex. hdr= IP() before giving the attributes
            for j in dict1[p][i]:		# This will add attributes to already created raw headers
                    k='hdr.'+j		# ex. hdr.src='1.1.1.1'
                    exec(k)
            h.append(hdr)
            #print(h)
  pkt=h[0]
  for j in range(1,len(h)):
    pkt= pkt/h[j]
  pkt.show()

geneatingPacket()
