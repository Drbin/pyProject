import pandas as pd
df = pd.read_excel('1.xls')
data = df.ix[0].values
print("读取指定行的数据：\n{0}".format(data))