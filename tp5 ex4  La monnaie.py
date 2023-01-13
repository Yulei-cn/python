target=int(input("entez combine :"))

print(target,"euros,") 

money=[100,50,10,5,2,1]#纸币种类
number=[0,0,0,0,0,0]#纸币种类
for i in range(6):# 排循环，从最大面值开始考虑
    number[i]= target//money[i]#取整，算出当前面值可以找的最大张数
    target=target%money[i]#取余，算出当前面值找零后剩下的钱数

for i in range(6):
    print("c'est donc", money[i], "billets", number[i],)


