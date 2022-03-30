"""
2.2.1.6 Multiple inheritance — the LAB
https://edube.org/learn/python-advanced-1/multiple-inheritance-the-lab
"""


class Scanner:
    @staticmethod
    def scan():
        print('scan() method from Scanner class')


class Printer:
    @staticmethod
    def print():
        print('print() method from Printer class')


class Fax:
    @staticmethod
    def print():
        print('print() method from Fax class')

    @staticmethod
    def send():
        print('send() method from Fax class')


class MfdSpf(Scanner, Printer, Fax):
    pass


class MfdSfp(Scanner, Fax, Printer):
    pass


if __name__ == "__main__":
    mfd_spf = MfdSpf()
    mfd_sfp = MfdSfp()
    mfd_spf.scan()
    mfd_spf.print()
    mfd_spf.send()
    mfd_sfp.scan()
    mfd_sfp.print()
    mfd_sfp.send()
