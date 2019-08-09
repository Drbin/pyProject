def file_on(data):
    data = data.encode()
    f = open("logs.txt", "a")
    f.write(data)
    f.close()
    return 0