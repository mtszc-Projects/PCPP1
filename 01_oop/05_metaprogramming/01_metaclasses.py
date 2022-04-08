"""
5.1.1.10 Metaprogramming – LAB: meta classes
https://edube.org/learn/python-advanced-1/metaprogramming-lab-metaclasses
"""
from datetime import datetime


def get_instantiation_time(self):
    return self.instantiation_time


class MetaClass(type):
    instantiated_classes = []

    def __new__(mcs, name, bases, dictionary):
        if 'get_instantiation_time' not in dictionary:
            dictionary['get_instantiation_time'] = get_instantiation_time
        obj = super().__new__(mcs, name, bases, dictionary)
        obj.instantiation_time = datetime.now().strftime('%Y-%m-%d %H:%M:%S')
        mcs.instantiated_classes.append(name)
        return obj


class MyClass1(metaclass=MetaClass):
    pass


class MyClass2(metaclass=MetaClass):
    pass


if __name__ == '__main__':
    from_meta_1 = MyClass1()
    from_meta_2 = MyClass2()
    print(MetaClass.instantiated_classes)
    print(from_meta_1.get_instantiation_time())
    print(from_meta_2.get_instantiation_time())
