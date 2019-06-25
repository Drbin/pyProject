row = int(input("请输入行数："))
for i in range(row):
    for _ in range(row-i-1):
        print(" ", end='')
    for _ in range(2*i+1):
        print("*", end='')
    print()
