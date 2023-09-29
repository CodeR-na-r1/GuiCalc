# written on py 3.11.5

# --- imports

from API.MyUI import UI
from Controllers.BaseController import BaseControllerImpl
from Controllers.KeyboardEventsController import KeyboardEventsControllerImpl
from Controllers.GachiSoundController import GachiSoundControllerImpl
from Controllers.NormalSoundController import NormalSoundControllerImpl

# --- main code

# creating dependencies
controller = BaseControllerImpl()
keyboardEvents = KeyboardEventsControllerImpl()
gachiSoundController = GachiSoundControllerImpl()
normalSoundController = NormalSoundControllerImpl()

# create ui with di
ui = UI(controller=controller, keyboardEvents=keyboardEvents, soundController=gachiSoundController)

ui.createWindow()

ui.setLayout()

ui.enableKeyEvents()

ui.mainloop()