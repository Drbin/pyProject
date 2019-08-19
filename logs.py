def file_on(data):
    #data = data.encode()
    f = open("logs.txt", "a+")
    f.write(data+"\n")
    f.close()
file_on('dsad')