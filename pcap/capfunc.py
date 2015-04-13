#!/usr/bin/env python

'''
capfunc.py (A supportive module Created by Harsh Dattani <github.com/harhsdattani> used to make capture.py a bit small) 
'''

import pcapy
def devices():
    global list_devices
    list_devices = pcapy.findalldevs()
    return list_devices

def select(devices_s):
    if devices_s >= len(list_devices):
      print 'Aha.. I know your are fuzzing with me! Select proper devices'
      return 'false'
    else:
      return 'true'

def timecheck(): 
    timeout = raw_input('Enter time to capture: ')   
    try:
      int(timeout)
      timeout = int(timeout)
      return timeout 
    except ValueError:
      return 'false'

