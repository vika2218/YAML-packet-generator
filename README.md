# YAML-packet-generator
The main goal of this code is to remove complexity of scapy.
Scapy is flexible packet generation module for generating any kind of packet.
With the help of this code, we can generate packet using YAML template. 
YAML templates are easy to read and use. Just change/add headers/attributes in YAML template and packet is ready for you.

YAML-packet-generator contains 2 files : packet_generator.yaml (Make changes in this file) and packet_generator.py


packet_generator.py generates packets flexibly without relying on specific functions for each packet headers. 

Scalability: Very flexible as well as scalable. No need to add extra header in future because this code will support all the headers and packet definitions supported by scapy module.




