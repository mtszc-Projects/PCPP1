"""
1.2.1.1 Working with class and instance data – instance variables — the LAB
https://edube.org/learn/python-advanced-1/working-with-class-and-instance-data-instance-variables-2
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
