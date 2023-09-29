from Interfaces.IBaseController import IBaseController
import math
from enum import Enum, auto

class BaseControllerImpl(IBaseController):

    class LastState(Enum):
        DigitInput = auto(),
        OperandInput = auto(),
        EvalSkipped = auto(),
        Eval = auto()

    def __init__(self, floatPrecision = 10) -> None:

        self.floatPrecision = floatPrecision

        self.lastState = BaseControllerImpl.LastState.Eval
        self.lastComputingState = BaseControllerImpl.LastState.Eval

        self.error = False
        self.m_initMantissa = False

        self.savedOperand: float = 0
        self.operand: float = 0
        self.operator: str = "="

    def isError(self) -> bool:
        return self.error
    
    def setError(self):
        self.error = True
    
    def getValue(self) -> float:

        self.operand = self.__roundFloat(self.operand)

        return self.operand
    
    def invertAssign(self) -> float:

        self.operand = -self.operand

        return self.operand

    def addDigit(self, digit: int) -> float:

        if (self.lastState == self.LastState.OperandInput
            or self.lastState == self.LastState.Eval):
            self.savedOperand = self.operand
            self.operand = 0

        # self.operand *= 10
        # if self.operand >= 0:
        #     self.operand += digit
        # else:
        #     self.operand -= digit

        tempOperand = str(self.operand)

        if self.m_initMantissa:
            tempOperand += "."
            self.m_initMantissa = False

        tempOperand += str(digit)
        self.__convertOperand(tempOperand)
        
        self.lastState = self.LastState.DigitInput

        return self.getValue()
    
    def removeLastDigit(self) -> float:

        # if self.operand < 0:
        #     self.operand = -self.operand
        #     self.operand = self.operand // 10
        #     self.operand = -self.operand
        # else:
        #     self.operand = self.operand // 10

        tempOperand = str(self.operand)

        if self.m_initMantissa and "." not in tempOperand:
            self.m_initMantissa = False
            return self.operand

        if len(tempOperand) > 0:
            tempOperand = tempOperand[:-1]

            if len(tempOperand) > 0 and tempOperand[-1] == ".":
                tempOperand = tempOperand[:-1]

            if tempOperand == "":
                tempOperand = "0"

            self.__convertOperand(tempOperand)

        return self.getValue()

    def initMantissa(self) -> str:
        
        res = str(self.operand)

        if "." not in res:
            res += "."
            self.m_initMantissa = True

        return res

    def rootSquare(self) -> float:

        self.operand = math.sqrt(self.operand)

        return self.getValue()

    def square(self) -> float:

        self.operand = self.operand ** 2

        return self.getValue()

    def reset(self):

        self.lastState = BaseControllerImpl.LastState.Eval
        self.lastComputingState = BaseControllerImpl.LastState.Eval

        self.error = False

        self.savedOperand = 0
        self.operand = 0
        self.operator = "="

    def setOp(self, op: str):

        if self.lastComputingState == self.LastState.OperandInput and self.lastState != self.LastState.OperandInput:
            self.lastState = self.LastState.EvalSkipped
            self.calc()

        self.lastState = self.LastState.OperandInput
        self.lastComputingState = BaseControllerImpl.LastState.OperandInput
        self.operator = op

    def calc(self) -> float:

        match self.lastState:
            case self.LastState.DigitInput:
                newSaved = self.operand
                self.__ALU()
                self.savedOperand = newSaved
            case self.LastState.Eval:
                saved = self.savedOperand
                self.operand, self.savedOperand = self.savedOperand, self.operand  # Если операнд не ввели, то вторым операндом должен быть последний введенный, поэтому swap-аем
                self.__ALU()
                self.savedOperand = saved
            case self.LastState.OperandInput:
                saved = self.operand
                self.savedOperand = self.operand
                self.__ALU()
                self.savedOperand = saved
            case self.LastState.EvalSkipped:
                self.__ALU()

        self.lastState = self.LastState.Eval
        self.lastComputingState = BaseControllerImpl.LastState.Eval

        return self.getValue()
        
    def __ALU(self):

        match self.operator:
            case "+":
                self.operand = self.savedOperand + self.operand
            case "-":
                self.operand = self.savedOperand - self.operand
            case "*":
                self.operand = self.savedOperand * self.operand
            case "/":
                if self.operand != 0:
                    self.operand = self.savedOperand / self.operand
                else:
                    self.error = True
            case "=":
                ...

    def __convertOperand(self, newValue: str):

        if "." in newValue:
            self.operand = float(newValue)
        else:
            self.operand = int(newValue)
        
    def __roundFloat(self, value) -> float:

        baseLen = len(str(int(value)))
        needPrecision = self.floatPrecision - baseLen - 1 # 1 == len point

        if needPrecision > 0:
            return round(value, needPrecision)
        else:
            return self.operand