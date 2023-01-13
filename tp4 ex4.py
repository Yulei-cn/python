'''
a = [2, 7, 5, 6, 7, 1, 6, 2, 1, 7, 6]
maxlabel = max(a,key=a.count)
sum=0
for i in a:
    if i == maxlabel:
        sum+=1
print("Le nombre le plus frequent dans la liste est le :  (%s x)" % sum )

l = [2, 7, 5, 6, 7, 1, 6, 2, 1, 7, 6,6,6]
cl = Counter(l)
for k, v in cl.items():
    if v > 1:
        print("元素{}, 重复{}次".format(k, v))

def counter(arr):
    return Counter(arr)
print(counter(arr))
'''

from collections import Counter
arr = [2, 7, 5, 6, 7, 1, 6, 2, 1, 7, 6,6,6]
n=Counter(arr)
print("Le nombre le plus frequent dans la liste est le  : %s "  %n.most_common(1))
