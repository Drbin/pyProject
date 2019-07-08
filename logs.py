def file_on(data):
    print(data)
    data = data.encode()
    f = open("logs.txt", "wb")
    f.write(data)
    f.close()
