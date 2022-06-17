"""
5.1.1.10 Metaprogramming – LAB: meta classes
https://edube.org/learn/python-advanced-1/metaprogramming-lab-metaclasses
Imagine you’ve been given a task to clean up the code of a system developed in Python – the code should be treated as
legacy code;
the system was created by a group of volunteers who worked with no clear “clean coding” rules;
the system suffers from a problem: we don’t know in which order the classes are created, so it causes multiple
dependency problems;
your task is to prepare a metaclass that is responsible for:
equipping all newly instantiated classes with time stamps, persisted in a class attribute named instantiation_time;
equipping all newly instantiated classes with the get_instantiation_time() method. The method should return the value
of the class attribute instantiation_time.
* The metaclass should have its own class variable (a list) that contains a list of the names of the classes
instantiated by the metaclass (tip: append the class name in the __new__ method).
Your metaclass should be used to create a few distinct legacy classes;
create objects based on the classes;
list the class names that are instantiated by your metaclass.
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
