#!/usr/bin/env python
'''  Capture.py
  
  Created by Harsh Dattani <github.com/harhsdattani>
  D.T. 13/04/205
  
  This program is free software; you can redistribute it and/or modify
  it under the terms of the GNU General Public License as published by
  the Free Software Foundation; either version 2 of the License, or
  (at your option) any later version.
  
  This program is distributed in the hope that it will be useful,
  but WITHOUT ANY WARRANTY; without even the implied warranty of
  MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
  GNU General Public License for more details.
  
  You should have received a copy of the GNU General Public License
  along with this program; if not, write to the Free Software
  Foundation, Inc., 51 Franklin Street, Fifth Floor, Boston,
  MA 02110-1301, USA '''

import capfunc
import pcapy
from impacket.ImpactDecoder import *
from struct import *
import time

def main():
     print '\n\t\nKnow source and destination of packet communicating with'
     devices = capfunc.devices()
     print '\nSelect from list of adapters\n'
     for i in devices:
       print devices.index(i), i
     devices_s = int(raw_input('Waiting for you to select Adapter!: '))
     ret = str(capfunc.select(devices_s))
     if ret == 'true':
       timeout = capfunc.timecheck()
       if timeout == 'false':
        print '\nI said dnt fuzz with me, Here is punishment, start from again'  
        main()
       t_ms = timeout*1000
       get_d = devices[devices_s]
       cap = pcapy.open_live(get_d , 65536 , 1 , t_ms)
       timeout = time.time() + timeout
       while (1):
        if time.time() > timeout:
          break
        try:
          (header, packet) = cap.next()
          eth_header = packet[:14] 
          eth = unpack('!6s6sH' , eth_header)
          source = decode_hex(eth_header[:6])
          dest = decode_hex(eth_header[6:12])
          print 'Source MAC address is', source, '  Destination MAC address is', dest
        except Exception,e:
          print 'Timeout in capturing this packet'           
     else:
        main()

def decode_hex (value_r) :
    b = "%.2x:%.2x:%.2x:%.2x:%.2x:%.2x" % (ord(value_r[0]) , ord(value_r[1]) , ord(value_r[2]), ord(value_r[3]), ord(value_r[4]) , ord(value_r[5]))
    return b
main()
