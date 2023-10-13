# task-1

class MyClass:
    orig_attr = 'Hello'

    def __init__(self):
        self.instance_attr = 'Hello instance'

    def hello_instance(self):
        return self.instance_attr + ' method'

    @staticmethod
    def hello_static(say_smth):
        return say_smth

    @classmethod
    def hello_class(cls):
        return cls.orig_attr + ' class method'

wolf = MyClass()

print(wolf.hello_instance())
print(MyClass.hello_static('Hello static method'))
print(MyClass.hello_class())



class Animals:
    favo_anim = []

    def __init__(self, *foo):
        self.favo_animIns = [foo]

    def anim_instance(self):
        return self.favo_animIns

    @staticmethod
    def anim_static(*bar):
        return [bar]

    @classmethod
    def anim_class(cls, favo):
        cls.favo_anim.append(favo)
        return cls.favo_anim

anim = Animals('panda', 'tipratikan')

print(anim.anim_instance())
print(Animals.anim_static('qo\'ng\'ir ayiq', 'oq ayiq'))
print(Animals.anim_class('yo\'lbars'))






class Place:
    p_n = 'Nature'

    def __init__(self):
        self.place = 'Sea'

    def place_ins(self):
        return self.place

    @staticmethod
    def place_sta(buzz):
        return buzz

    @classmethod
    def place_class(cls, char):
        return cls.p_n + ', ' + char

place = Place()

print(place.place_ins())
print(Place.place_sta('Ocean'))
print(Place.place_class('Forest'))