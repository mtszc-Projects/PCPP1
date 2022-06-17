"""
4.1.1.13 LAB #2
https://edube.org/learn/python-advanced-1/lab-2-1
The previous task was a very easy one. Now let's rework the code a bit:
introduce the Delicacy class to represent a generic delicacy. The objects of this class will replace the old school
dictionaries. Suggested attribute names: name, price, weight;
your class should implement the __str__() method to represent each object state;
experiment with the copy.copy() and deepcopy.copy() methods to see the difference in how each method copies objects.
"""
import copy


class Delicacy:
    def __init__(self, name='default_candy', price=0, weight=0):
        self.dictionary = {'name': name, 'price': price, 'weight': weight}

    def __str__(self):
        return f'Object state: {self.dictionary}'


warehouse = list()
warehouse.append({'name': 'Lolly Pop', 'price': 0.4, 'weight': 133})
warehouse.append({'name': 'Licorice', 'price': 0.1, 'weight': 251})
warehouse.append({'name': 'Chocolate', 'price': 1, 'weight': 601})
warehouse.append({'name': 'Sours', 'price': 0.01, 'weight': 513})
warehouse.append({'name': 'Hard candies', 'price': 0.3, 'weight': 433})

print('Source list of candies')
for item in warehouse:
    print(item)

warehouse_class = copy.deepcopy(warehouse)

print('Class list of candies')
for item in warehouse_class:
    delicacy = Delicacy(item['name'], item['price'], item['weight'])
    print(delicacy)
