"""
2.2.1.6 Multiple inheritance — the LAB
https://edube.org/learn/python-advanced-1/multiple-inheritance-the-lab
Your task is to build a multifunction device (MFD) class consisting of methods responsible for document scanning,
printing, and sending via fax.
The methods are delivered by the following classes:
    scan(), delivered by the Scanner class;
    print(), delivered by the Printer class;
    send() and print(), delivered by the Fax class.
Each method should print a message indicating its purpose and origin, like:
    'print() method from Printer class'
    'send() method from Fax class'
create an MFD_SPF class ('SPF' means 'Scanner', 'Printer', 'Fax'), then instantiate it;
create an MFD_SFP class ('SFP' means 'Scanner', 'Fax', 'Printer'), then instantiate it;
on each object call the methods: scan(), print(), send();
observe the output differences. Was the Printer class utilized each time?
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
