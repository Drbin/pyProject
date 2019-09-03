import threading


def run(num):
    print("running on number:%s" % num)


if __name__ == '__main__':
    t1 = threading.Thread(target=run, args=(1,))
    t2 = threading.Thread(target=run, args=(2,))
    t1.start()
    t2.start()
    print(t1.getName())  
    print(t2.getName())
