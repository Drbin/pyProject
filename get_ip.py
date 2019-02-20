import socket
import uuid

mac = uuid.UUID(int=uuid.getnode()).hex[-12:]
print(":".join([mac[e:e + 2] for e in range(0, 11, 2)]))
#获取本机电脑名
my_name = socket.getfqdn(socket.gethostname(  ))
#获取本机ip
my_addr = socket.gethostbyname(my_name)
print(myname)
print(my_addr)
