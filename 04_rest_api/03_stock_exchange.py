"""
2.1.1.3 New York Stock Exchange
https://edube.org/learn/pcpp1-working-with-restful-apis/new-york-stock-exchange
"""
import xml.etree.ElementTree

try:
    stock_exchange = xml.etree.ElementTree.parse('nyse.xml').getroot()
except FileNotFoundError:
    print("Sorry, there is no such file.")
except xml.etree.ElementTree.ParseError:
    print("Can't parse a file.")
dummy_var = ''
wide = 43
narrow = 13
print(f'COMPANY{dummy_var:<{wide-7}}', end='')
print(f'LAST{dummy_var:<{narrow-4}}', end='')
print(f'CHANGE{dummy_var:<{narrow-6}}', end='')
print(f'MIN{dummy_var:<{narrow-3}}', end='')
print(f'MAX{dummy_var:<{narrow-3}}')
print('-'*90)


for data in stock_exchange.findall('quote'):
    print(f'{data.text:<{wide}}', end='')
    last = data.attrib['last']
    print(f'{last:<{narrow}}', end='')
    change = data.attrib['change']
    print(f'{change:<{narrow}}', end='')
    min_value = data.attrib['min']
    print(f'{min_value:<{narrow}}', end='')
    max_value = data.attrib['max']
    print(f'{max_value:<{narrow}}')
