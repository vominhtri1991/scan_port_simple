import os
import socket
import platform
from datetime import datetime

rm_ip=input('Remote IP To Scan Port: ')
port_scan=input('Remote ports to scan (each port seperate by common ,): ')
os_sys=platform.system()
if(os_sys=='Windows'):
	cmd='ping -n 1 '+rm_ip
else:
	cmd='ping -c 1 '+rm_ip
res_ping=os.popen(cmd)
check_live=0
for line in res_ping.readlines():
	if("TTL=" in line):
		check_live=1
		break
if(check_live==0):
	print("Host: {} not online".format(rm_ip))
	exit(0)

print("Host: {} online now. Continue to scan port listen: ".format(rm_ip))
port_list=port_scan.split(',')
for port in port_list:
	s=socket.socket(socket.AF_INET,socket.SOCK_STREAM)
	socket.setdefaulttimeout(1)
	rs_port=s.connect_ex((rm_ip,int(port)))
	if (rs_port==0):
		print("Port {} is listen!!!".format(port))
