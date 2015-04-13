#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
#  hashing.py
#  
#  Copyright 2014 harsh <harsh@harsh-linux>
#  
#  This program is free software; you can redistribute it and/or modify
#  it under the terms of the GNU General Public License as published by
#  the Free Software Foundation; either version 2 of the License, or
#  (at your option) any later version.
#  
#  This program is distributed in the hope that it will be useful,
#  but WITHOUT ANY WARRANTY; without even the implied warranty of
#  MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
#  GNU General Public License for more details.
#  
#  You should have received a copy of the GNU General Public License
#  along with this program; if not, write to the Free Software
#  Foundation, Inc., 51 Franklin Street, Fifth Floor, Boston,
#  MA 02110-1301, USA.


import hashlib, sys
x = str(sys.argv[1:])
y = str(sys.argv[2:])
if y == "['sha512']":
	if len(sys.argv[2:]) > 0:
		x = hashlib.sha512(x).hexdigest()
		print x
elif y == "['md5']":
	if len(sys.argv[2:]) > 0:
		x = hashlib.md5(x).hexdigest()
		print x
elif y == "['sha1']":
	if len(sys.argv[2:]) > 0:
		x = hashlib.sha1(x).hexdigest()
		print x
elif y == "['sha224']":
	if len(sys.argv[2:]) > 0:
		x = hashlib.sha224(x).hexdigest()
		print x
elif y == "['sha256']":
	if len(sys.argv[2:]) > 0:
		x = hashlib.sha256(x).hexdigest()
		print x
elif y == "['sha384']":
	if len(sys.argv[2:]) > 0:
		x = hashlib.sha384(x).hexdigest()
		print x
else:
	print "\t lacks argument \n Use hashing.py argv1 argv2 \n \t \t argv1 = your text to find HASH \n \t \t argv2 = sha1 or sha224 or sha256 or sha384 or sha512 or md5"
