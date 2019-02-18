import socket
my_name = socket.getfqdn(socket.gethostname(  ))
my_addr = socket.gethostbyname(my_name)


def logs_on(data):
    #data = data.encode()
    f = open("logs.txt", "a+")
    f.write(data+"\n")
    f.close()

logs_on("在"+my_addr+"运行")

