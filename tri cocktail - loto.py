# python

def bubble_sort(iterable):
    for i in range(len(iterable) - 1, 0, -1):
        bubbled = 0

        for j in range(i):
            if iterable[j] > iterable[j + 1]:
                iterable[j], iterable[j + 1] = iterable[j + 1], iterable[j]
                bubbled = 1

        if not bubbled: break

    return iterable

bubble_sort([int(item) for item in user_input.split(' ')]))



  for n in range(5):
    for i in loto:
      for ii in loto1:
        if i == ii:
            a=True
            break          
        else:
            a=False
            break

if a==True:
  resulat.append(loto1)
else: 
  pass
print(resulat)
print(len(resulat))