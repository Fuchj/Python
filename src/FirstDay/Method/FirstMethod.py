def greet_user(username):
    """显示简单的问候语"""
    print("Hello, " + username.title() + "!")
#greet_user('jesse')

def SumShow(a,b):
    """求和方法"""
    return a+b 
#print(SumShow(1,2))
def JudgeMax(a,b):
    """比较两个数的大小"""
    if(a>=b):
        return a
    else:
        return b
#a=JudgeMax(33,66)
#print(a);
def NameHelper(FirstName,LastName):
    persion={"first":FirstName,"last":LastName}
    return persion
#name=NameHelper("Li","ming")
#print(name)

    # 首先创建一个列表，其中包含一些要打印的设计
    #unprinted_designs = ['iphone case', 'robot pendant', 'dodecahedron']
    #completed_models = []
    # 模拟打印每个设计，直到没有未打印的设计为止
    # 打印每个设计后，都将其移到列表completed_models中
    #while unprinted_designs:#只要列表unprinted_designs中还有设计,while循环就模拟
    #打印设计的过程
    current_design = unprinted_designs.pop()
    #模拟根据设计制作3D打印模型的过程
    #print("Printing model: " + current_design)
    #completed_models.append(current_design)
    #显示打印好的所有模型
    #print("\nThe following models have been printed:")
    #for completed_model in completed_models:
    #print(completed_model)
#unprinted_designs = ['iphone case', 'robot pendant', 'dodecahedron']
#completed_models=[]
def TestMethod(unprinted_designs,completed_models):
    while unprinted_designs:
          #打印设计的过程
        current_design = unprinted_designs.pop()
        #模拟根据设计制作3D打印模型的过程
        print("Printing model: " + current_design)
        completed_models.append(current_design)  
    #显示打印好的所有模型
    print("\nThe following models have been printed:")
    for completed_model in completed_models:
        print(completed_model)
#TestMethod(unprinted_designs,completed_models)

#print(completed_models)

def TestMethod(a):
    print("传递的类型",type(a))
    for x in a:
        print(x)
def TestMethod(a,b):
    """判断输入参数类型并遍历值"""
    print("传递a的类型",type(a),"传递b的类型",type(b))
    c=[a,b]
    for x in c:
        print(x)
#a=[11,12,13,14,15]
#b=(21,22,23,24,25)
#TestMethod(a,b)


