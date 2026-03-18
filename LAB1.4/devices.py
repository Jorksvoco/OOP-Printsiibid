from interfaces import Printer, Scanner

class MyPrinter(Printer):
    def print(self, document: str):
        print(f"Printer prindib: {document}")

class Photocopier(Printer, Scanner):
    def print(self, document: str):
        print(f"Paljundusmasin prindib: {document}")
        
    def scan(self, document: str):
        print(f"Paljundusmasin skaneerib: {document}")

class MultiFunctionMachine(Printer, Scanner):
    def __init__(self, printer: Printer, scanner: Scanner):
        self.printer = printer
        self.scanner = scanner

    def print(self, document: str):
        self.printer.print(document)

    def scan(self, document: str):
        self.scanner.scan(document)