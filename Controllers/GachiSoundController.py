from Interfaces.ISoundController import ISoundController

import winsound

class GachiSoundControllerImpl(ISoundController):

    def playSound(self, typeSound: ISoundController.TypeEvent) -> bool:

        match typeSound:
            case ISoundController.TypeEvent.btnEqual:
                winsound.PlaySound(".\\resources\\gachi\\ahhhhhhh.wav", winsound.SND_ASYNC)
            case ISoundController.TypeEvent.btnError:
                winsound.PlaySound(".\\resources\\gachi\\rip-ears.wav", winsound.SND_ASYNC)
            case ISoundController.TypeEvent.btnDigit:
                winsound.PlaySound(".\\resources\\gachi\\fuck-you1.wav", winsound.SND_ASYNC)
            case ISoundController.TypeEvent.btnOperand:
                winsound.PlaySound(".\\resources\\gachi\\oh-shit-iam-sorry.wav", winsound.SND_ASYNC)
            case ISoundController.TypeEvent.btnOverFlow:
                winsound.PlaySound(".\\resources\\gachi\\rip-ears.wav", winsound.SND_ASYNC) 
            case ISoundController.TypeEvent.btnReset:
                winsound.PlaySound(".\\resources\\gachi\\woo.wav", winsound.SND_ASYNC)