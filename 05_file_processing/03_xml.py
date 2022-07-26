"""
2.2.1.1 LAB: XML – Lab 1
https://edube.org/learn/pcpp1-5/lab-xml-lab-1
Have you seen the weather forecast for the coming week? It’ll be an extremely sunny and warm week. Familiarize yourself
with the data in the forecast.xml file and then complete the following tasks:
Create a class named TemperatureConverter and its convert_celsius_to_fahrenheit method.
The convert_celsius_to_fahrenheit method should convert the temperature from Celsius to Fahrenheit. Use the following
formula:
F = 9/5 * C + 32.
Create a class named ForecastXmlParser and its parse method responsible for reading data from forecast.xml. Use the
TemperatureConverter class to convert the temperature from Celsius to Fahrenheit (rounded to one decimal place). The
parse method should print the following results:
Monday: 28 Celsius, 82.4 Fahrenheit
Tuesday: 27 Celsius, 80.6 Fahrenheit
Wednesday: 28 Celsius, 82.4 Fahrenheit
Thursday: 29 Celsius, 84.2 Fahrenheit
Friday: 29 Celsius, 84.2 Fahrenheit
Saturday: 32 Celsius, 89.6 Fahrenheit
Sunday: 33 Celsius, 91.4 Fahrenheit
NOTE: The forecast.xml file is available in your working directory at Edube Interactive. If you want to download the
file and work with it locally, you can do it here: forecast.xml
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
