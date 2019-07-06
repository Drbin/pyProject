
def file_on(data):
    print(data)
    f = open("logs.txt", "wb")
    f.write(data)
    f.close()
file_on("测试数据")