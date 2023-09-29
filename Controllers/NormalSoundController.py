from Interfaces.ISoundController import ISoundController

import winsound

class NormalSoundControllerImpl(ISoundController):

    def playSound(self, typeSound: ISoundController.TypeEvent) -> bool:

        match typeSound:
            case ISoundController.TypeEvent.btnEqual:
                winsound.PlaySound(".\\resources\\just\\click1.wav", winsound.SND_ASYNC)
            case ISoundController.TypeEvent.btnError:
                winsound.PlaySound(".\\resources\\just\\click2.wav", winsound.SND_ASYNC)
            case ISoundController.TypeEvent.btnDigit:
                winsound.PlaySound(".\\resources\\just\\click1.wav", winsound.SND_ASYNC)
            case ISoundController.TypeEvent.btnOperand:
                winsound.PlaySound(".\\resources\\just\\click3.wav", winsound.SND_ASYNC)
            case ISoundController.TypeEvent.btnOverFlow:
                winsound.PlaySound(".\\resources\\just\\click4.wav", winsound.SND_ASYNC) 
            case ISoundController.TypeEvent.btnReset:
                winsound.PlaySound(".\\resources\\just\\click4.wav", winsound.SND_ASYNC)