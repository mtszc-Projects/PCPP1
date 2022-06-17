"""
4.1.1.12 LAB #1
https://edube.org/learn/python-advanced-1/lab-1-1
Introduction:
Imagine you have been hired to help run a candy warehouse.
The task:
Your task is to write a code that will prepare a proposal of reduced prices for the candies whose total weight exceeds
300 units of weight (we don’t care whether those are kilograms or pounds)
Your input is a list of dictionaries; each dictionary represents one type of candy. Each type of candy contains a key
entitled 'weight', which should lead you to the total weight details of the given delicacy. The input is presented in
the editor;
Prepare a copy of the source list (this should be done with a one-liner) and then iterate over it to reduce the price
of each delicacy by 20% if its weight exceeds the value of 300;
Present an original list of candies and a list that contains the proposals;
Check if your code works correctly when copying and modifying the candy item details.
Expected output:
Source list of candies
{'name': 'Lolly Pop', 'price': 0.4, 'weight': 133}
{'name': 'Licorice', 'price': 0.1, 'weight': 251}
{'name': 'Chocolate', 'price': 1, 'weight': 601}
{'name': 'Sours', 'price': 0.01, 'weight': 513}
{'name': 'Hard candies', 'price': 0.3, 'weight': 433}
******************
Price proposal
{'name': 'Lolly Pop', 'price': 0.4, 'weight': 133}
{'name': 'Licorice', 'price': 0.1, 'weight': 251}
{'name': 'Chocolate', 'price': 0.8, 'weight': 601}
{'name': 'Sours', 'price': 0.008, 'weight': 513}
{'name': 'Hard candies', 'price': 0.24, 'weight': 433}
"""
import copy

warehouse = list()
warehouse.append({'name': 'Lolly Pop', 'price': 0.4, 'weight': 133})
warehouse.append({'name': 'Licorice', 'price': 0.1, 'weight': 251})
warehouse.append({'name': 'Chocolate', 'price': 1, 'weight': 601})
warehouse.append({'name': 'Sours', 'price': 0.01, 'weight': 513})
warehouse.append({'name': 'Hard candies', 'price': 0.3, 'weight': 433})

print('Source list of candies')
for item in warehouse:
    print(item)

print('\nPrice proposal')
warehouse_proposal = copy.deepcopy(warehouse)
for item in warehouse_proposal:
    if item['weight'] > 300:
        item['price'] *= 0.8
    print(item)

warehouse_proposal[0]['name'] = 'Candies'

print(warehouse)
print(warehouse_proposal)
