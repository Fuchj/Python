
my_list = [0,1, 2,3,4, 5,6, 7,8, 9,10,11]
my_list1=[11,10,9,8,7,6,5,4,3,2,1,0]
def binary_search(list, item):
    '''二分查找 
    list:数组列表
    item：要查询的值    
    '''
    num=0#定义查询需要的次数
    low_index = 0 #查找范围的索引下限
    high_index = len(list)-1#查找范围的索引上限
    while low_index <= high_index: #只要范围没有缩小到只包含一个元素
        num+=1#没查询一次，次数加1
        mid = (low_index + high_index)//2#向下取整 
        guess = list[mid]#猜测的值
        if guess == item: #当猜测的值和要查询的值相等时返回元素索引
            return "的索引为"+str(mid)+",查询次数为"+str(num)
        if guess > item: #当猜测的值大于要查询的值相等时，说明猜测值的索引大于要查询值的索引，需要把查询范围的上限缩小
            high_index = mid - 1
        else: #当猜测的值小于要查询的值相等时，说明猜测值的索引小于要查询值的索引，需要把查询范围的下限增大
            low_index = mid + 1

    return "值在数组中不存在,查询次数为"+str(num) 
#print (binary_search(my_list, 1))
def findSmallest(arr):
    '''查找最小值元素的索引'''
    smallest = arr[0]
    smallest_index = 0    
    a=range(1,len(arr) )
    for i in a:
        if arr[i] < smallest:
            smallest = arr[i]
            smallest_index = i
    return smallest_index
#result=findSmallest(my_list)
def selectSortMethod(arry):
    '''选择排序'''
    newArry=[]
    for x in range(len(arry)):
        smallest = findSmallest(arry)
        newArry.append(arry.pop(smallest))
    return newArry 
print(selectSortMethod(my_list1));
print (binary_search(my_list, 1))