#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
#  check.py
#  
#  Run this program as python check.py
#  It will generate a list of all visible files in folder residing check.py, if you want a list of all files including hidden #  files, then comment out if not condition and rerun program.
#  	#	#	#	#	#	#	#	#	#	#	#	#	#	#	#	
import pickle
import os
import hashlib

dirs = os.listdir('.')
file_o = open('list.txt','w')

for file in dirs:
  if not ((file.endswith('.py')) or (file.endswith('~')) or (file.startswith('.'))):
    print file
    file_o.write('\n')
    hash_file = hashlib.sha512(open(file).read()).hexdigest()
    file_o.write('hash value is of %s is %s ' %(file, hash_file))
