from Interfaces.IKeyboardEventsController import IKeyboardEventsController

class KeyboardEventsControllerImpl(IKeyboardEventsController):

    btns = None
    digitCallback = None
    serviceCallback = None

    @staticmethod
    def initHandler(btns, digitCallback, serviceCallback):
        KeyboardEventsControllerImpl.btns = btns
        KeyboardEventsControllerImpl.digitCallback = digitCallback
        KeyboardEventsControllerImpl.serviceCallback = serviceCallback

    @staticmethod
    def eventHandler(event):
        # print(f"key == {event.char}, ord == {ord(event.char)}")

        KeyboardEventsControllerImpl.serviceCallback("@")

        if event.char != "":
            match event.char:
                case "1" | "2" | "3" | "4" | "5" | "6" | "7" | "8" | "9" | "0":
                    KeyboardEventsControllerImpl.digitCallback(digit=event.char)
                case "=" | "+" | "-" | "/" | "*":
                    KeyboardEventsControllerImpl.serviceCallback(mnemonic=event.char)
                case "c":
                    KeyboardEventsControllerImpl.serviceCallback(mnemonic="C")
                case ".":
                    KeyboardEventsControllerImpl.serviceCallback(mnemonic=".")

            match ord(event.char):
                case 8:
                    KeyboardEventsControllerImpl.serviceCallback("←")
                case 13:
                    KeyboardEventsControllerImpl.serviceCallback("=")