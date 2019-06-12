"""一个可用于表示Dog的类"""
class Dog():
    """新建Dog类"""
    def __init__(self, name, age):
        """初始化属性name和age"""
        self.name = name
        self.age = age
    def sit(self):
        """模拟小狗被命令时蹲下"""
        print(self.name.title() + " is now sitting.")
    def roll_over(self):
        """模拟小狗被命令时打滚"""
        print(self.name.title() + " rolled over!")
    def test_method(self):
        '''测试方法'''
        return "ok"
'''
    my_dog = Dog('willie', 6)
    my_dog.sit()
    my_dog.roll_over()
    data1=my_dog.test_method()
    print("end")
'''
class BenDog(Dog):
    """新建BenDog类,继承Dog类"""
    def __init__(self, name, age,height):
        """初始化父类属性,再初始化特有的属性height"""
        super().__init__(name, age)
        self.height=height
    def MyNew(self):
        """BenDog 特有方法"""
        print("My height is:%s"%self.height)
'''
    my_ben=BenDog("benben",2,130)
    my_ben.MyNew()
    my_ben.roll_over()
    my_ben.height=180
    my_ben.MyNew()
'''
