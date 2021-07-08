# Interface Segregation Principle
from abc import abstractmethod


class Machine:

    def print(self, document):
        raise NotImplementedError

    def fax(self, document):
        raise NotImplementedError

    def scan(self, document):
        raise NotImplementedError


def MultiFunctionPrinter(Machine):

    def print(self, document):
        pass

    def fax(self, document):
        pass

    def scan(self, document):
        pass


def OldFashionPrinter(Machine):

    def print(self, document):
        # Ok
        pass

    def fax(self, document):
        pass  # noop

    def scan(self, document):
        """If i cannot use this method, why can i see ? """
        """Not supported!"""
        raise NotImplementedError('Printer cannot scan!')


# Solution Part
class Printer:
    @abstractmethod
    def print(self, documet):
        pass


class Scanner:
    @abstractmethod
    def scan(self, document):
        pass


class MyPrinter(Printer):
    def print(self, document):
        print(document)


class Photocopier(Printer, Scanner):
    def print(self, document):
        pass

    def scan(self, document):
        pass


class MultiFunctionDevice(Printer, Scanner):
    @abstractmethod
    def print(self, document):
        pass

    @abstractmethod
    def scan(self, document):
        pass


class MultiFunctionMachine(MultiFunctionDevice):
    def __init__(self, printer: Printer, scanner: Scanner) -> None:
        super().__init__()
        self.scanner = scanner
        self.printer = printer

    def print(self, document):
        self.printer.print(document)

    def scan(self, document):
        self.scanner.scan(document)
