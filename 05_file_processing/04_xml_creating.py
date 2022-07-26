"""
2.4.1.1 LAB: XML – Lab 2
https://edube.org/learn/pcpp1-5/lab-xml-lab-2
You are a programmer working for an online store. Your task is to build an XML document containing information about the
three vegan products available in the store:
<?xml version="1.0"?>
<shop>
    <category name="Vegan Products">
        <product name="Good Morning Sunshine">
            <type>cereals</type>
            <producer>OpenEDG Testing Service</producer>
            <price>9.90</price>
            <currency>USD</currency>
        </product>
        <product name="Spaghetti Veganietto">
            <type>pasta</type>
            <producer>Programmers Eat Pasta</producer>
            <price>15.49</price>
            <currency>EUR</currency>
        </product>
        <product name="Fantastic Almond Milk">
            <type>beverages</type>
            <producer>Drinks4Coders Inc.</producer>
            <price>19.75</price>
            <currency>USD</currency>
        </product>
    </category>
</shop>
Save the document to the shop.xml file. Use UTF-8 character encoding and don't forget to add the prolog to the beginning
of the file. Good luck!
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
