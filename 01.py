import math
count = 0
while (count <5):
    count = count + 1
    s=input("输入一个数：")
    s=float(s)
    if s>=0:
      s=math.sqrt(s)#计算
      print("平方根是：",s)
    else:
      print("负数不能开平方根")