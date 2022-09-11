# TODO: Inheriting from list
class IntegerList(list):

    @staticmethod
    def check_value_type(value):
        if type(value) is not int:
            raise ValueError('Not an integer type')

    def __setitem__(self, index, value):
        IntegerList.check_value_type(value)
        list.__setitem__(self, index, value)

    def append(self, value):
        IntegerList.check_value_type(value)
        list.append(self, value)

    def extend(self, iterable):
        for element in iterable:
            IntegerList.check_value_type(element)

        list.extend(self, iterable)


int_list = IntegerList()

int_list.append(66)
int_list.append(22)
print('Appending int elements succeed:', int_list)

int_list[0] = 49
print('Inserting int element succeed:', int_list)

int_list.extend([2, 3])
print('Extending with int elements succeed:', int_list)

try:
    int_list.append('8-10')
except ValueError:
    print('Appending string failed')

try:
    int_list[0] = '10/11'
except ValueError:
    print('Inserting string failed')

try:
    int_list.extend([997, '10/11'])
except ValueError:
    print('Extending with ineligible element failed')

print('Final result:', int_list)

# TODO: Inheriting from dictionary
# from datetime import datetime
#
#
# class MonitoredDict(dict):
#     def __init__(self, *args, **kwargs):
#         super().__init__(*args, **kwargs)
#         self.log = list()
#         self.log_timestamp('MonitoredDict created')
#
#     def __getitem__(self, key):
#         val = super().__getitem__(key)
#         self.log_timestamp('value for key [{}] retrieved'.format(key))
#         return val
#
#     def __setitem__(self, key, val):
#         super().__setitem__(key, val)
#         self.log_timestamp('value for key [{}] set'.format(key))
#
#     def log_timestamp(self, message):
#         timestampStr = datetime.now().strftime("%Y-%m-%d (%H:%M:%S.%f)")
#         self.log.append('{} {}'.format(timestampStr, message))
#
#
# kk = MonitoredDict()
# kk[10] = 15
# kk[20] = 5
#
# print('Element kk[10]:', kk[10])
# print('Whole dictionary:', kk)
# print('Our log book:\n')
# print('\n'.join(kk.log))

# TODO: IBAN validator inheritance from Exception and dict
# import random
#
#
# class IBANValidationError(Exception):
#     pass
#
#
# class IBANDict(dict):
#     def __setitem__(self, _key, _val):
#         if validateIBAN(_key):
#             super().__setitem__(_key, _val)
#
#     def update(self, *args, **kwargs):
#         for _key, _val in dict(*args, **kwargs).items():
#             self.__setitem__(_key, _val)
#
#
# def validateIBAN(iban):
#     iban = iban.replace(' ', '')
#
#     if not iban.isalnum():
#         raise IBANValidationError("You have entered invalid characters.")
#
#     elif len(iban) < 15:
#         raise IBANValidationError("IBAN entered is too short.")
#
#     elif len(iban) > 31:
#         raise IBANValidationError("IBAN entered is too long.")
#
#     else:
#         iban = (iban[4:] + iban[0:4]).upper()
#         iban2 = ''
#         for ch in iban:
#             if ch.isdigit():
#                 iban2 += ch
#             else:
#                 iban2 += str(10 + ord(ch) - ord('A'))
#         ibann = int(iban2)
#
#         if ibann % 97 != 1:
#             raise IBANValidationError("IBAN entered is invalid.")
#
#         return True
#
#
# my_dict = IBANDict()
# keys = ['GB72 HBZU 7006 7212 1253 00', 'FR76 30003 03620 00020216907 50', 'DE02100100100152517108']
#
# for key in keys:
#     my_dict[key] = random.randint(0, 1000)
#
# print('The my_dict dictionary contains:')
# for key, value in my_dict.items():
#     print("\t{} -> {}".format(key, value))
#
# try:
#     my_dict.update({'dummy_account': 100})
# except IBANValidationError:
#     print('IBANDict has protected your dictionary against incorrect data insertion')
