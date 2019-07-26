from SuanFa.algorithm  import KuaiPai
from time import sleep
#my_list = [10,11, 12,13,14, 15,16, 17,18, 19,20,21]
#my_list1=[21,20,19,18,17,16,15,14,13,12,11,10]
my_list2=[11,10,11,18,15,16,15,14,13,12,20,10]
#print(KuaiPai(my_list))
#print(KuaiPai(my_list1))

try:
    #countdown(10)
    arry= KuaiPai(my_list2)
    print(arry)
    for x in arry:
        print(x)
        sleep(1)

    print("结束-----------------------------------------------")
except Exception as e:
    print('Invalid input:', e)
    print ('Please try again-----------------------------------------------')