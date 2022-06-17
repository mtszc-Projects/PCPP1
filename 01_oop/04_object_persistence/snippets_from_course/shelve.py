"""
4.3.1.2 Serialization of Python objects using the shelve module
https://edube.org/learn/python-advanced-1/serialization-of-python-objects-using-the-shelve-module
"""
import shelve

shelve_name = 'first_shelve.shlv'

my_shelve = shelve.open(shelve_name, flag='c')
my_shelve['EUR'] = {'code': 'Euro', 'symbol': '€'}
my_shelve['GBP'] = {'code': 'Pounds sterling', 'symbol': '£'}
my_shelve['USD'] = {'code': 'US dollar', 'symbol': '$'}
my_shelve['JPY'] = {'code': 'Japanese yen', 'symbol': '¥'}
my_shelve.close()

new_shelve = shelve.open(shelve_name)
print(new_shelve['USD'])
new_shelve.close()
