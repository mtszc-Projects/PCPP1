import xml.etree.ElementTree as ET

# TODO: Change tag
tree = ET.parse('books.xml')
root = tree.getroot()
for child in root:
    child.tag = 'movie'
    print(child.tag, child.attrib)
    for sub_child in child:
        print(sub_child.tag, ':', sub_child.text)

# TODO: remove()
# tree = ET.parse('books.xml')
# root = tree.getroot()
# for child in root:
#     child.tag = 'movie'
#     child.remove(child.find('author'))
#     child.remove(child.find('year'))
#     print(child.tag, child.attrib)
#     for sub_child in child:
#         print(sub_child.tag, ':', sub_child.text)

# TODO: set() attribute
# tree = ET.parse('books.xml')
# root = tree.getroot()
# for child in root:
#     child.tag = 'movie'
#     child.remove(child.find('author'))
#     child.remove(child.find('year'))
#     child.set('rate', '5')
#     print(child.tag, child.attrib)
#     for sub_child in child:
#         print(sub_child.tag, ':', sub_child.text)

# TODO: write()
# tree = ET.parse('books.xml')
# root = tree.getroot()
# for child in root:
#     child.tag = 'movie'
#     child.remove(child.find('author'))
#     child.remove(child.find('year'))
#     child.set('rate', '5')
#     print(child.tag, child.attrib)
#     for sub_child in child:
#         print(sub_child.tag, ':', sub_child.text)
#
# tree.write('movies.xml', 'UTF-8', True)
