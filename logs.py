
def file_on(data):
    f = open("logs.txt", "wb")
    f.write(data)
    return 0