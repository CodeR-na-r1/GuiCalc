from abc import ABC

class IKeyboardEventsController(ABC):

    @staticmethod
    def initHandler(btns, digitCallback, serviceCallback):
        pass

    @staticmethod
    def eventHandler(event):
        pass