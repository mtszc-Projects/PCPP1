"""
2.2.1.1 LAB: XML – Lab 1
https://edube.org/learn/pcpp1-5/lab-xml-lab-1
"""
import xml.etree.ElementTree as ET


class TemperatureConverter:
    @staticmethod
    def convert_celsius_to_fahrenheit(celsius):
        fahrenheits = 9/5 * celsius + 32
        return fahrenheits


class ForecastXmlParser:
    @staticmethod
    def parse(file):
        temperature_converter = TemperatureConverter()
        tree = ET.parse(file)
        root = tree.getroot()
        for child in root:
            print(child[0].text, ": ",
                  child[1].text, ' Celsius, ',
                  "{:.1f}".format(temperature_converter.convert_celsius_to_fahrenheit(int(child[1].text))),
                  ' Fahrenheit', sep='')


forecast_xml_parser = ForecastXmlParser()
forecast_xml_parser.parse('forecast.xml')
