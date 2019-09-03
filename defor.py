import threading
import time


def run(num):

    print("running on number:%s" % num)

    time.sleep(3)


if __name__ == '__main__':
    t1 = threading.Thread(target=run, args=(1,))
    t2 = threading.Thread(target=run, args=(2,))

    t1.start()  #
    t2.start()  #

    print(t1.getName())  #
    print(t2.getName())
