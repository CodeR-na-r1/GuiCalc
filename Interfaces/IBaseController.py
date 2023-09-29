from abc import ABC, abstractmethod

class IBaseController(ABC):

    @abstractmethod
    def isError(self) -> bool:
        pass

    @abstractmethod
    def setError(self):
        pass
    
    @abstractmethod
    def getValue(self) -> float:
        pass
    
    @abstractmethod
    def invertAssign(self) -> float:
        pass

    @abstractmethod
    def addDigit(self, digit: int) -> float:
        pass
    
    @abstractmethod
    def removeLastDigit(self) -> float:
        pass

    @abstractmethod
    def initMantissa() -> str:
        pass

    @abstractmethod
    def rootSquare(self) -> float:
        pass

    @abstractmethod
    def square(self) -> float:
        pass

    @abstractmethod
    def reset(self):
        pass

    @abstractmethod
    def setOp(self, op: str):
        pass

    @abstractmethod
    def calc(self) -> float:
        pass