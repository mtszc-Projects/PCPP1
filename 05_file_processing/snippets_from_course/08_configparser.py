import configparser

# TODO: Default parsing with sections()
config = configparser.ConfigParser()
print(config.read('config.ini'))

print('Sections:', config.sections(), '\n')

print('mariadb section:')
print('Host:', config['mariadb']['host'])
print('Database:', config['mariadb']['name'])
print('Username:', config['mariadb']['user'])
print('Password:', config['mariadb']['password'], '\n')

print('redis section:')
print('Host:', config['redis']['host'])
print('Port:', int(config['redis']['port']))
print('Database number:', int(config['redis']['db']))

# TODO: read config from dictionary
# config = configparser.ConfigParser()
#
# dict = {
#     'DEFAULT': {
#         'host': 'localhost'
#     },
#     'mariadb': {
#         'name': 'hello',
#         'user': 'root',
#         'password': 'password'
#     },
#     'redis': {
#         'port': 6379,
#         'db': 0
#     }
# }
#
# config.read_dict(dict)
#
# print('Sections:', config.sections(), '\n')
#
# print('mariadb section:')
# print('Host:', config['mariadb']['host'])
# print('Database:', config['mariadb']['name'])
# print('Username:', config['mariadb']['user'])
# print('Password:', config['mariadb']['password'], '\n')
#
# print('redis section:')
# print('Host:', config['redis']['host'])
# print('Port:', int(config['redis']['port']))
# print('Database number:', int(config['redis']['db']))

# TODO: create and modify config file
# config = configparser.ConfigParser()
#
# config['DEFAULT'] = {'host': 'localhost'}
# config['mariadb'] = {'name': 'hello',
#                      'user': 'root',
#                      'password': 'password'}
# config['redis'] = {'port': 6379,
#                    'db': 0}
# # TODO: CREATING
# with open('config2.ini', 'w') as configfile:
#     config.write(configfile)
#
# # TODO: MODIFYING
# config.read('config2.ini')
# config['redis']['db'] = '1'
# with open('config2.ini', 'w') as configfile:
#     config.write(configfile)
