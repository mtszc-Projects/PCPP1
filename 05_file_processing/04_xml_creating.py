"""
2.4.1.1 LAB: XML – Lab 2
https://edube.org/learn/pcpp1-5/lab-xml-lab-2
"""
import xml.etree.ElementTree as ET


class Product:
    def __init__(self, category, name, type_name, producer, price, currency):
        product = ET.SubElement(category, 'product', {'name': f'{name}'})
        self.type_name = ET.SubElement(product, 'type')
        self.type_name.text = type_name
        self.producer = ET.SubElement(product, 'producer')
        self.producer.text = producer
        self.price = ET.SubElement(product, 'price')
        self.price.text = price
        self.currency = ET.SubElement(product, 'currency')
        self.currency.text = currency


root = ET.Element('shop')
category_vegan = ET.SubElement(root, 'category', {'name': 'Vegan Products'})
product_01 = Product(category_vegan, 'good_morning_sunshine', 'cereals', 'OpenEDG Testing Service', '9.90', 'USD')
product_02 = Product(category_vegan, 'Spaghetti Veganietto', 'pasta', 'Programmers Eat Pasta', '15.49', 'EUR')
product_03 = Product(category_vegan, 'Fantastic Almond Milk', 'beverages', 'Drinks4Coders Inc.', '19.75', 'USD')
ET.dump(root)
tree = ET.ElementTree(root)
tree.write('shop.xml', 'UTF-8', True)
