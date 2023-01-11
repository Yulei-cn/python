'''
a = [2, 7, 5, 6, 7, 1, 6, 2, 1, 7, 6]
maxlabel = max(a,key=a.count)
sum=0
for i in a:
    if i == maxlabel:
        sum+=1
print(maxlabel,  "(%s x)" % sum )
'''

a = [2, 7, 5, 6, 7, 1, 6, 2, 1, 7, 6]
elm_count = a.count(7)
print("Il y a 7 (%s x) " % elm_count)
