
#name = "Hello Python Crash Course world!"

#print(name.title())
#name = "ada lovelace"
#print(name.title())

age = 23
#数字和字符串拼接，会发生错误 
#message = "Happy " + age + "rd Birthday!" 
#使用str 把非字符串的类型转换为字符串
message = "Happy " + str(age) + "rd Birthday!"
print(message)
print("--------------------------------------")
a="ss"
arry=[1,a,"订单",1.2]
print(arry)

print(arry[2])

print(arry[-1])
print(arry[-4])
arry[-1]="我是最后一个"
print(arry)
arry.append("新来的")
print(arry)
print("--------------------------------------")
print(arry)
del arry[-1]
print(arry)

print("-------删除-------------------------------")
#arry.pop(-1)
#print(arry)

#a= arry.pop(-1)
#print(arry);
#print(a)
#arry.append(a);
#print(arry);


arry.append("1");
print(arry)
#打印列表的长度
print("列表arry的长度："+str(len(arry)))

#----------循环编列列表-------------
print("开始循环遍历")
for x in arry:
    print(x)

print("----------range()方法-------------")
#range(1,6) 

arry1=list(range(2,11,2))
print(arry1)


#把1~11范围中的数字的平方存放到列表中
arry2= [value**2 for value in range(1,11)]
print(arry2)
[1, 4, 9, 16, 25, 36, 49, 64, 81, 100]



