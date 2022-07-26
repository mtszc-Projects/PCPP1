"""
5.2.1.1 LAB: Interpolating values – Lab 1
https://edube.org/learn/pcpp1-5/lab-interpolating-values-lab-1
Imagine a situation in which you receive a configuration file containing access data for various services.
Unfortunately, the file is a terrible mess, because it contains data used in both production and development
environments.
Your task will be to create two files named prod_config.ini and dev_config.ini. The prod_config.ini file should only
contain sections for the production environment, while dev_config.ini should only contain sections for the development
environment.
To distinguish between the environments, use the env option added to all sections in the mess.ini file. The env option
should be removed from the sections before moving them to the files.
Expected result
The prod_config.ini file:
[sentry]
key = key
secret = secret
[github]
user = user
password = password
The dev_config.ini file:
[mariadb]
host = localhost
name = hello
user = user
password = password
[redis]
host = localhost
port = 6379
db = 0
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
