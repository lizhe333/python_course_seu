"""
定义一个抽象类Animal 定义Mammal和Bird两个类继承Animal, 分别定义多
个这两个类特有的方法和成员– 定义Dog和Parrot两个类分别继承Mammal和Bird，
在Dog类中定义方法访问和修改Mammal类中的成员
"""
from abc import ABC, abstractmethod
class Animal(ABC):
    def __init__(self,a,b):
        #共有的名字属性
        self.name = a
        self.age = b
    @abstractmethod
    def sound(self):
        pass


#哺乳类
class Mammal(Animal):
    def __init__(self,a,b,c="哺乳类"):
        super().__init__(a,b)
        self.category = c  #哺乳类特有属性
        self.energy = 100  #哺乳类共有属性
    
    #特有方法
    def is_running(self):
        return f"{self.name} is running."
    
    #重写抽象类里面的方法
    def sound(self):
        return "Mammal sound"

class dog(Mammal):
    def play(self):
        #修改父类的属性
        self.energy -= 10
        return f"{self.name} is playing. Energy left: {self.energy}"
    
    def make_sound(self):
        return "Woof Woof!"
    
class Bird(Animal):
    def __init__(self,a,b,c="鸟类"):
        super().__init__(a,b)
        self.category = c  #鸟类特有属性
        self.wing_span = 50  #鸟类共有属性
    
    #特有方法
    def is_flying(self):
        return f"{self.name} is flying."
    
    #重写抽象类里面的方法
    def sound(self):
        return "Bird sound"

class Parrot(Bird):
    def talk(self):
        return f"{self.name} says: Hello!"
    
    def make_sound(self):
        return "Squawk!"
#测试代码
if __name__ == "__main__":
    dog1 = dog("Buddy", 3)

    print(dog1.is_running())
    print(dog1.play())
    print(dog1.make_sound())

    parrot1 = Parrot("Polly", 2)

    print(parrot1.is_flying())
    print(parrot1.talk())
    print(parrot1.make_sound())
        


      
        