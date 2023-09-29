from abc import ABC, abstractmethod
from enum import Enum, auto

class ISoundController(ABC):

    class TypeEvent(Enum):
        
        btnEqual = auto(),
        btnDigit = auto(),
        btnError = auto(),
        btnOverFlow = auto(),
        btnOperand = auto(),
        btnReset = auto()

    @abstractmethod
    def playSound(self) -> bool:
        pass