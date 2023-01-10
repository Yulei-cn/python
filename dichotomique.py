#https://www.runoob.com/python3/python-binary-search.html
#dichotomique  récursif

# 返回 x 在 arr 中的索引，如果不存在返回 -1
def binarySearch (arr, l, r, x): 
  
    # 基本判断
    if r >= l: 
  
        mid = int(l + (r - l)/2)
  
        # 元素整好的中间位置
        if arr[mid] == x: 
            return mid 
          
        # 元素小于中间位置的元素，只需要再比较左边的元素
        elif arr[mid] > x: 
            return binarySearch(arr, l, mid-1, x) 
  
        # 元素大于中间位置的元素，只需要再比较右边的元素
        else: 
            return binarySearch(arr, mid+1, r, x) 
  
    else: 
        # 不存在
        return -1
  
# 测试数组
arr = [ 2, 3, 4, 10, 40 ] 
x = 10
  
# 函数调用
result = binarySearch(arr, 0, len(arr)-1, x) 
  
if result != -1: 
    print ("元素在数组中的索引为 %d" % result )
else: 
    print ("元素不在数组中")

    
#dichotomique    itératif
'''
编写函数，用二分法在有序列表中查找元素，
找到则返回下标，找不到则返回-1。
编写主程序，输入列表元素，调用第2题的函数排序，输入一个数，
调用本题的函数查找。列表输入一次，查找可输入多次。尝试用递归实现
written by tyb
2020/10/20
references:https://www.runoob.com/python3/python-binary-search.html
'''
from Lab43 import selectionSort,inputList
# 返回 x 在 arr 中的索引，如果不存在返回 -1
def binarySearch(arr, l, r, x):
    # 基本判断
    if r >= l:
        mid = int(l + (r - l) / 2)
        # 元素整好的中间位置
        if arr[mid] == x:
            return mid
            # 元素小于中间位置的元素，只需要再比较左边的元素
        elif arr[mid] > x:
            return binarySearch(arr, l, mid - 1, x)
            # 元素大于中间位置的元素，只需要再比较右边的元素
        else:
            return binarySearch(arr, mid + 1, r, x)
    else:
        # 不存在
        return -1
if __name__ == '__main__':
    list = inputList()
    list = selectionSort(list)
    print("排好序的列表为：",list)
    x = int(input("输入要查找的数："))
    bSearch = binarySearch(list,0,len(list)-1,x)
    if bSearch != -1:
        print("元素在数组中的索引为: %d" %bSearch)
    else:
        print("元素不在数组中")

def inputList():
    #num_list = list(map(int, input().split()))  # 或者
    print("请输入整数，以空格隔开")
    num_list = [int(i) for i in input().split()] # 接收一段以空格隔开的整数的输入
    return num_list
def findMin(list):
    num_min = list[0] #记录最小值
    j = 0  #记录取得最小值时的下标
    for i in range(len(list)):
        if list[i] <= num_min:
            num_min = list[i]
            j = i
    return num_min,j
def selectionSort(list):
    new_list = [] #排好序的列表
    for i in range(len(list)):
        min, j = findMin(list)
        new_list.append(min)
        del list[j]
    return new_list
def outputList(list):
    for i in range(len(list)):
        print(list[i])
if __name__ == '__main__':
    list = inputList()
    list = selectionSort(list)
    print(list)
    outputList(list)
    #min,j = findMin(list)
    #print("最小值为：%d，对应的下标为%d"%(min,j))

