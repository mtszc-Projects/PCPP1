import xml.etree.ElementTree as ET

# TODO: Creating Element object and dump()
root = ET.Element('data')
ET.dump(root)

# TODO: SubElement()
# root = ET.Element('data')
# movie_1 = ET.SubElement(root, 'movie', {'title': 'The Little Prince', 'rate': '5'})
# movie_2 = ET.SubElement(root, 'movie', {'title': 'Hamlet', 'rate': '5'})
# ET.dump(root)
# tree = ET.ElementTree(root)
# tree.write('creating.xml', 'UTF-8', True)
