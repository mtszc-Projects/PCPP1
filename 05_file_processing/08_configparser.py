"""
5.2.1.1 LAB: Interpolating values – Lab 1
https://edube.org/learn/pcpp1-5/lab-interpolating-values-lab-1
"""
import configparser


def create_dicts_from_ini_file(file_name):
    config = configparser.ConfigParser()
    config.read(file_name)
    production = {}
    development = {}
    for section in config.sections():
        if config[section]['env'] == 'dev':
            development[section] = {}
            for _ in config[section]:
                development[section].update(config[section])
            del development[section]['env']
        else:
            production[section] = {}
            for _ in config[section]:
                production[section].update(config[section])
            del production[section]['env']
    return production, development


def create_file_from_dict(dictionary, file_name):
    config = configparser.ConfigParser()
    for key in dictionary.keys():
        config[key] = dictionary[key]
    with open(file_name, 'w') as configfile:
        config.write(configfile)


prod, dev = create_dicts_from_ini_file('mess.ini')
create_file_from_dict(prod, 'prod_config.ini')
create_file_from_dict(dev, 'dev_config.ini')
