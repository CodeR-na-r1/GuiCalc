from tkinter import *

from Interfaces.IBaseController import IBaseController
from Interfaces.IKeyboardEventsController import IKeyboardEventsController
from Interfaces.ISoundController import ISoundController

from functools import partial
from API.HoverButton import HoverButton

class UI:

    def __init__(self, controller: IBaseController, keyboardEvents: IKeyboardEventsController, soundController: ISoundController) -> None:
        self.window: Tk | None = None

        self.LENGTH_MAX_NUMBER = 10

        self.btnsText = [ "C", "√x", "x^2", "←",
                 "7", "8", "9", "*",
                 "4", "5", "6", "-",
                 "1", "2", "3", "+",
                 "+/-", "0", "/", "=", 
               ]

        self.btnsDict = {}

        self.controller: IBaseController = controller

        self.keyboardEvents: IKeyboardEventsController = keyboardEvents

        self.soundController = soundController

    def createWindow(self):
        
        self.window = Tk(screenName="Calculator")
        
        self.window.geometry("325x475")
        self.window.title("Калькулятор")

    def setLayout(self):
        
        self.__initGrid()
        self.__initWidgets()
        self.__setLayout()

    def mainloop(self):
        
        self.window.mainloop()

    def enableKeyEvents(self):

        self.keyboardEvents.initHandler(self.btnsText, partial(self.__btnDigitCallback), partial(self.__btnServiceCallback))
        self.window.bind("<Key>", self.keyboardEvents.eventHandler)

    def disableKeyEvents(self):

        self.window.unbind("<Key>")

    def __initGrid(self):

        self.window.rowconfigure(index=0, weight=2)

        # row config
        for row in range(2, 7):
            self.window.rowconfigure(index=row, weight=1)

        # column config
        for col in range(4):
            self.window.columnconfigure(index=col, weight=1)

    def __initWidgets(self):

        self.inputField = Entry(self.window, justify="right", font="Calibri 42")
        self.inputField.insert(0, "0")
        self.inputField["bg"] = "#FFF"
        
        for btnText in self.btnsText:

            self.btnsDict[btnText] = HoverButton(self.window, text=btnText, hoverColor="#E2E2E2", backgroundColor="#FDFDFD", borderwidth=0, command=
                                                (partial(self.__btnDigitCallback, btnText))
                                                if btnText.isdigit()
                                                else (partial(self.__btnServiceCallback, btnText)))
            self.btnsDict[btnText]["bg"] = "#FFF"

        self.btnsDict["="].setHoverColor("#9A99DC")

    def __setLayout(self):

        self.inputField.grid(row=0, column=0, rowspan=2, columnspan=4, sticky='nesw')

        btnIndex = 0
        for row in range(2, 7, 1):
            for col in range(0, 4, 1):
                self.btnsDict[self.btnsText[btnIndex]].grid(row=row, column=col, padx=1, pady=1, sticky='nesw')
                btnIndex += 1

    def __showControllerValue(self, value = None):
        if value == None:
            value = self.controller.getValue()
        
        self.inputField.delete(0, END)

        if self.controller.isError():
            self.inputField.insert(0, "Error")
            self.soundController.playSound(self.soundController.TypeEvent.btnError)
        elif len(str(value)) > self.LENGTH_MAX_NUMBER:
            self.inputField.insert(0, "OverFlow")
            self.controller.setError()
            self.soundController.playSound(self.soundController.TypeEvent.btnOverFlow)
        else:
            self.inputField.insert(0, str(value))

    def __btnDigitCallback(self, digit: str):

        self.soundController.playSound(self.soundController.TypeEvent.btnDigit)
        
        self.controller.addDigit(int(digit))
        self.__showControllerValue()

    def __btnServiceCallback(self, mnemonic: str):

        match mnemonic:
            case "+/-":
                self.controller.invertAssign()
                self.__showControllerValue()
            case "=":
                self.controller.calc()
                self.__showControllerValue()
                self.soundController.playSound(self.soundController.TypeEvent.btnEqual)
            case "C":
                self.controller.reset()
                self.__showControllerValue()
                self.soundController.playSound(self.soundController.TypeEvent.btnReset)
            case "x^2":
                self.controller.square()
                self.__showControllerValue()
            case "√x":
                self.controller.rootSquare()
                self.__showControllerValue()
            case "←":
                self.controller.removeLastDigit()
                self.__showControllerValue()
            case ".":
                value = self.controller.initMantissa()
                self.__showControllerValue(value=value)
            case "@":   # just update display
                self.__showControllerValue()
            case _:
                self.controller.setOp(mnemonic)
                self.__showControllerValue()
                self.soundController.playSound(self.soundController.TypeEvent.btnOperand)