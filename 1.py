import math
while True:
    r = float(input('请输入半径: '))
    S = math.pi*math.pow(r,2)
    print("以%d为半径的圆 面积是%d" % (r, S))
    C = 2*math.pi*r
    