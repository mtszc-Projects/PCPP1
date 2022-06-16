"""
2.6.1.8 LAB
https://edube.org/learn/python-advanced-1/lab-1
You are about to create a multifunction device (MFD) that can scan and print documents;
the system consists of a scanner and a printer;
your task is to create blueprints for it and deliver the implementations;
create an abstract class representing a scanner that enforces the following methods:
    scan_document – returns a string indicating that the document has been scanned;
    get_scanner_status – returns information about the scanner (max. resolution, serial number)
Create an abstract class representing a printer that enforces the following methods:
    print_document – returns a string indicating that the document has been printed;
    get_printer_status – returns information about the printer (max. resolution, serial number)
Create MFD1, MFD2 and MFD3 classes that inherit the abstract classes responsible for scanning and printing:
    MFD1 – should be a cheap device, made of a cheap printer and a cheap scanner, so device capabilities (resolution)
    should be low;
    MFD2 – should be a medium-priced device allowing additional operations like printing operation history, and the
    resolution is better than the lower-priced device;
    MFD3 – should be a premium device allowing additional operations like printing operation history and fax machine.
Instantiate MFD1, MFD2 and MFD3 to demonstrate their abilities. All devices should be capable of serving generic feature
sets.
"""
import abc


class Scanner(abc.ABC):
    __serial_number = ''
    __max_resolution = ''

    @staticmethod
    @abc.abstractmethod
    def scan_document():
        return 'Document has been scanned from abstract Scanner.'

    @classmethod
    @abc.abstractmethod
    def get_scanner_status(cls):
        return cls.__max_resolution, cls.__serial_number


class Printer(abc.ABC):
    __serial_number = ''
    __max_resolution = ''

    @staticmethod
    @abc.abstractmethod
    def print_document():
        return 'Document has been printed from abstract Printer.'

    @classmethod
    @abc.abstractmethod
    def get_printer_status(cls):
        return cls.__max_resolution, cls.__serial_number


class Fax(abc.ABC):
    __serial_number = ''
    __max_resolution = ''

    @staticmethod
    @abc.abstractmethod
    def fax_document():
        return 'Document has been faxed from abstract Fax.'

    @classmethod
    @abc.abstractmethod
    def get_fax_status(cls):
        return cls.__max_resolution, cls.__serial_number


class MFD1(Scanner, Printer):
    __serial_number = 'MFD1000'
    __scanner_max_resolution = '150dpi'
    __printer_max_resolution = '300dpi'

    @staticmethod
    def scan_document():
        print(Scanner.scan_document())
        return 'Document has been scanned from MFD1.'

    @classmethod
    def get_scanner_status(cls):
        return f'Scanner max resolution {cls.__scanner_max_resolution}, device sn: {cls.__serial_number}'

    @staticmethod
    def print_document():
        print(Printer.print_document())
        return 'Document has been printed from MFD1.'

    @classmethod
    def get_printer_status(cls):
        return f'Printer max resolution {cls.__printer_max_resolution}, device sn: {cls.__serial_number}'


class MFD2(Scanner, Printer):
    __serial_number = 'MFD2000'
    __printing_counter = 0
    __scanner_max_resolution = '300dpi'
    __printer_max_resolution = '600dpi'

    @staticmethod
    def scan_document():
        print(Scanner.scan_document())
        return 'Document has been scanned from MFD2.'

    @classmethod
    def get_scanner_status(cls):
        return f'Scanner max resolution {cls.__scanner_max_resolution}, device sn: {cls.__serial_number}'

    @classmethod
    def print_document(cls):
        cls.__printing_counter += 1
        print(Printer.print_document())
        return 'Document has been printed from MFD2.'

    @classmethod
    def get_printer_status(cls):
        return f'Printer max resolution {cls.__printer_max_resolution}, device sn: {cls.__serial_number}'

    @classmethod
    def printing_operation_history(cls):
        return f'Device printed {cls.__printing_counter} documents till now.'


class MFD3(Scanner, Printer, Fax):
    __serial_number = 'MFD3000'
    __printing_counter = 0
    __scanner_max_resolution = '600dpi'
    __printer_max_resolution = '1200dpi'
    __fax_max_resolution = '1200dpi'

    @staticmethod
    def scan_document():
        print(Scanner.scan_document())
        return 'Document has been scanned from MFD3.'

    @classmethod
    def get_scanner_status(cls):
        return f'Scanner max resolution {cls.__scanner_max_resolution}, device sn: {cls.__serial_number}'

    @classmethod
    def print_document(cls):
        cls.__printing_counter += 1
        print(Printer.print_document())
        return 'Document has been printed from MFD3.'

    @classmethod
    def get_printer_status(cls):
        return f'Printer max resolution {cls.__printer_max_resolution}, device sn: {cls.__serial_number}'

    @classmethod
    def printing_operation_history(cls):
        return f'Device printed {cls.__printing_counter} documents till now.'

    @staticmethod
    def fax_document():
        print(Fax.fax_document())
        return 'Document has been scanned from MFD3.'

    @classmethod
    def get_fax_status(cls):
        return f'Fax max resolution {cls.__fax_max_resolution}, device sn: {cls.__serial_number}'


if __name__ == "__main__":
    mfd1 = MFD1()
    print(mfd1.scan_document())
    print(mfd1.get_scanner_status())
    print(mfd1.print_document())
    print(mfd1.get_printer_status())
    mfd2 = MFD2()
    print(mfd2.scan_document())
    print(mfd2.get_scanner_status())
    print(mfd2.print_document())
    print(mfd2.get_printer_status())
    print(mfd2.printing_operation_history())
    mfd3 = MFD3()
    print(mfd3.scan_document())
    print(mfd3.get_scanner_status())
    print(mfd3.print_document())
    print(mfd3.get_printer_status())
    print(mfd3.printing_operation_history())
    print(mfd3.fax_document())
    print(mfd3.get_fax_status())
