import random as r

class Fish:
    def __init__(self):
        self.x=r.randint(0,10)
        self.y=r.randint(0,10)
    def move(self):
        self.x-=1
        print("我的位置是",self.x,self.y)
class Goldfish(Fish):
    pass
class Carp(Fish):
    pass
class Salmon(Fish):
    pass
class Shark(Fish):
    def __init__(self):
        super().__init__()
        self.hungry=True
    def eat(self):
        if self.hungry:
            print("天天吃就不饿了")
            self.hungry=False
        else:
            print("吃饱了")
