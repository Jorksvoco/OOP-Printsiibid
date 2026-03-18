from abc import ABC, abstractmethod

class Printer(ABC):
    @abstractmethod
    def print(self, document: str):
        pass

class Scanner(ABC):
    @abstractmethod
    def scan(self, document: str):
        pass

class Fax(ABC):
    @abstractmethod
    def fax(self, document: str):
        pass