def file_on(data):
    data = data.encode()
    f = open("logs.txt", "wb")
    f.write(data)
    f.close()
    return 0