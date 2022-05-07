import xml.etree.ElementTree

# TODO: reading xml
cars_for_sale = xml.etree.ElementTree.parse('cars.xml').getroot()
print(cars_for_sale.tag)
for car in cars_for_sale.findall('car'):
    print('\t', car.tag)
    for prop in car:
        print('\t\t', prop.tag, end='')
        if prop.tag == 'price':
            print(prop.attrib, end='')
    print(' =', prop.text)


# TODO: changing xml
# tree = xml.etree.ElementTree.parse('cars.xml')
# cars_for_sale = tree.getroot()
# for car in cars_for_sale.findall('car'):
#     if car.find('brand').text == 'Ford' and car.find('model').text == 'Mustang':
#         cars_for_sale.remove(car)
#         break
# new_car = xml.etree.ElementTree.Element('car')
# xml.etree.ElementTree.SubElement(new_car, 'id').text = '4'
# xml.etree.ElementTree.SubElement(new_car, 'brand').text = 'Maserati'
# xml.etree.ElementTree.SubElement(new_car, 'model').text = 'Mexico'
# xml.etree.ElementTree.SubElement(new_car, 'production_year').text = '1970'
# xml.etree.ElementTree.SubElement(new_car, 'price', {'currency': 'EUR'}).text = '61800'
# cars_for_sale.append(new_car)
# tree.write('newcars.xml', method='')
