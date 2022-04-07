# !usr/bin/python
# 面向对象 类
class Animal():
    type_name = "Animal"

    def __init__(self, name, sex, age):
        self._name = name
        self._sex = sex
        self._age = age
        print(self.type_name+'---'+self._name+" is created")

    def _work(self):
        print(self._name, "can eat")

    def __del__(self):
        print(self.type_name+'---'+self._name+" is died")
    pass

# 继承


class Human(Animal):

    type_name = "Human"
    __bag = 'weapon'  # pravite

    def _work(self):
        print(self._name, "can work")

    def _call(self, x):
        print(self._name+" say:"+x+" I have "+self.__bag)

    # 内部类
    class Bad(Animal):
        type_name = "Badman"
        __bag = 'weapon'

        @classmethod  # 可直接用
        def _laugh(self):
            print("hahahahahahaha")

        def __call__(self):
            print("hahahahaha")
    pass


# 子类
class Child(Human):
    type_name = "Child"

    def _cry(self, x):
        super()._call(x)  # 调用了super内存中的__bag
    pass


class Cat(Animal):
    pass


def main():
    Human.Bad._laugh()
    hum1 = Human('ming', 'man', 18)
    hum2 = Child('xing', 'man', 1)
    hum3 = Human.Bad('ting', 'woman', 17)
    hum3()
    hum1._work()
    hum1._call("haha")
    hum2._work()
    hum2._cry("555555")
    # print(hum1.__bag) cant work
    cat1 = Cat("huahua", 'woman', 4)
    cat1._work()
    print(hasattr(hum3, 'kill'))  # judge if method kill in function hum3
    n = getattr(hum3, 'kill', 'dont exist')
    print(n)
    # delete attr ---------delattr(hum3,'kill')
    # add attr---------setattr(hum3,'job','killer')
    pass


if __name__ == "__main__":
    main()
    pass
