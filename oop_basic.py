
class car:
    def __init__(self,whel,color,quest):
        print("Begins")
        self.__whel=whel
        self.color=color
        self.quest=quest
    def fun(self):
        print("it is working")
    def __str__(self):
        return f"(whel:{self.__whel},color:{self.color},quest?:{self.quest})"
    def get_whel(self):
        print("wheeling",self.__whel)
        
c=car("eight","black","mileage")
print(c)
c.get_whel
