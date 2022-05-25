import xml.etree.ElementTree as ET

tree = ET.parse('books.xml')
root = tree.getroot()
# root = ET.fromstring(your_xml_as_string)
# TODO: Iteration over tree object
print('The root tag is:', root.tag)
print('The root has the following children:')
for child in root:
    print(child.tag, child.attrib)

# TODO: Indexing objects
print("My books:\n")
for book in root:
    print('Title: ', book.attrib['title'])
    print('Author:', book[0].text)
    print('Year: ', book[1].text, '\n')

# TODO: iter method
for author in root.iter('author'):
    print(author.text)

# TODO: findall method
for author in root.findall('author'):
    print(author.text)

# TODO: find method
print(root.find('book').get('title'))
