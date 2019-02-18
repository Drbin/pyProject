import socket
my_name = socket.getfqdn(socket.gethostname(  ))
my_addr = socket.gethostbyname(my_name)


def logs_on(data):
    #data = data.encode()
    f = open("logs.txt", "a+")
    f.write(my_addr+"\n")
    f.write(data+"\n")
    f.close()



