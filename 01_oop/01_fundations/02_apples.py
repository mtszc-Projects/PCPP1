"""
1.2.1.1 Working with class and instance data – instance variables — the LAB
https://edube.org/learn/python-advanced-1/working-with-class-and-instance-data-instance-variables-2
Imagine that you receive a task description of an application that monitors the process of apple packaging
before the apples are sent to a shop. A shop owner has asked for 1000 apples, but the total weight limitation
cannot exceed 300 units. Write a code that creates objects representing apples as long as both limitations are met.
When any limitation is exceeded, then the packaging process is stopped, and your application should print the number
of apple class objects created, and the total weight.
Your application should keep track of two parameters:
    the number of apples processed, stored as a class variable;
    the total weight of the apples processed; stored as a class variable. Assume that each apple's weight is random,
    and can vary between 0.2 and 0.5 of an imaginary weight unit;
"""
import random


class Apple:
    total_weight = 0
    total_amount = 0

    def __init__(self):
        self.weight = random.uniform(0.2, 0.5)
        Apple.total_weight += self.weight
        Apple.total_amount += 1


def packaging():
    while Apple.total_weight <= 300 and Apple.total_amount <= 1000:
        Apple()
    return Apple


packaging_stats = packaging()

print(f'Total amount of packed apples is: {packaging_stats.total_amount} pieces.'
      f'\nTotal weight of packed apples is: {round(packaging_stats.total_weight, 2)} units.')
