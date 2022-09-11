# TODO: Internal wrapper
# def simple_decorator(own_function):
#
#     def internal_wrapper(*args, **kwargs):
#         print('"{}" was called with the following arguments'.format(own_function.__name__))
#         print('\t{}\n\t{}\n'.format(args, kwargs))
#         own_function(*args, **kwargs)
#         print('Decorator is still operating')
#
#     return internal_wrapper
#
#
# @simple_decorator
# def combiner(*args, **kwargs):
#     print("\tHello from the decorated function; received arguments:", args, kwargs)
#
#
# combiner('a', 'b', exec='yes')


# TODO: decorator with argument
# def warehouse_decorator(material):
#     def wrapper(our_function):
#         def internal_wrapper(*args):
#             print('<strong>*</strong> Wrapping items from {} with {}'.format(our_function.__name__, material))
#             our_function(*args)
#             print()
#         return internal_wrapper
#     return wrapper
#
#
# @warehouse_decorator('kraft')
# def pack_books(*args):
#     print("We'll pack books:", args)
#
#
# @warehouse_decorator('foil')
# def pack_toys(*args):
#     print("We'll pack toys:", args)
#
#
# @warehouse_decorator('cardboard')
# def pack_fruits(*args):
#     print("We'll pack fruits:", args)
#
#
# pack_books('Alice in Wonderland', 'Winnie the Pooh')
# pack_toys('doll', 'car')
# pack_fruits('plum', 'pear')


# TODO: Decorator stacking
# def big_container(collective_material):
#     def wrapper(our_function):
#         def internal_wrapper(*args):
#             our_function(*args)
#             print('<strong>*</strong> The whole order would be packed with', collective_material)
#             print()
#         return internal_wrapper
#     return wrapper
#
#
# def warehouse_decorator(material):
#     def wrapper(our_function):
#         def internal_wrapper(*args):
#             our_function(*args)
#             print('<strong>*</strong> Wrapping items from {} with {}'.format(our_function.__name__, material))
#         return internal_wrapper
#     return wrapper
#
#
# @big_container('plain cardboard')
# @warehouse_decorator('bubble foil')
# def pack_books(*args):
#     print("We'll pack books:", args)
#
#
# @big_container('colourful cardboard')
# @warehouse_decorator('foil')
# def pack_toys(*args):
#     print("We'll pack toys:", args)
#
#
# @big_container('strong cardboard')
# @warehouse_decorator('cardboard')
# def pack_fruits(*args):
#     print("We'll pack fruits:", args)
#
#
# pack_books('Alice in Wonderland', 'Winnie the Pooh')
# pack_toys('doll', 'car')
# pack_fruits('plum', 'pear')

# TODO: class as decorator
# class SimpleDecorator:
#     def __init__(self, own_function):
#         self.func = own_function
#
#     def __call__(self, *args, **kwargs):
#         print('"{}" was called with the following arguments'.format(self.func.__name__))
#         print('\t{}\n\t{}\n'.format(args, kwargs))
#         self.func(*args, **kwargs)
#         print('Decorator is still operating')
#
#
# @SimpleDecorator
# def combiner(*args, **kwargs):
#     print("\tHello from the decorated function; received arguments:", args, kwargs)
#
#
# combiner('a', 'b', exec='yes')


# TODO: class as decorator with arguments
# class WarehouseDecorator:
#     def __init__(self, material):
#         self.material = material
#
#     def __call__(self, own_function):
#         def internal_wrapper(*args, **kwargs):
#             print('<strong>*</strong> Wrapping items from {} with {}'.format(own_function.__name__, self.material))
#             own_function(*args, **kwargs)
#             print()
#         return internal_wrapper
#
#
# @WarehouseDecorator('kraft')
# def pack_books(*args):
#     print("We'll pack books:", args)
#
#
# @WarehouseDecorator('foil')
# def pack_toys(*args):
#     print("We'll pack toys:", args)
#
#
# @WarehouseDecorator('cardboard')
# def pack_fruits(*args):
#     print("We'll pack fruits:", args)
#
#
# pack_books('Alice in Wonderland', 'Winnie the Pooh')
# pack_toys('doll', 'car')
# pack_fruits('plum', 'pear')


# TODO: decorating a class
# def object_counter(class_):
#     class_.__getattr__orig = class_.__getattribute__
#
#     def new_getattr(self, name):
#         if name == 'mileage':
#             print('We noticed that the mileage attribute was read')
#         return class_.__getattr__orig(self, name)
#
#     class_.__getattribute__ = new_getattr
#     return class_
#
#
# @object_counter
# class Car:
#     def __init__(self, VIN):
#         self.mileage = 0
#         self.VIN = VIN
#
#
# car = Car('ABC123')
# print('The mileage is', car.mileage)
# print('The VIN is', car.VIN)
