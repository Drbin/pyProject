
def file_on(data):
    print(data)
    f = open("logs.txt", "wb")
    f.write(data)
    f.close()
