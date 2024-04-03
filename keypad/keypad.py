from keypad_driver import KeyPad
from I2C_Screen import updateScreen
from time import time, sleep_ms

keyPad = KeyPad(8, 9, 10, 11, 12, 13, 14, 15)

validationOption = ["A", "B"]

def waitKeyPad(ignoreStartTimeout = False, screenText = None, keyLength = 3):
    keyIn = ""
    startTime = time()
    while True:
        if ((not ignoreStartTimeout) or len(keyIn)) and (time() - startTime > 30):
            return "timeout"
        
        keyData = getKey()
        # Optimisation vu qu'on utilise pas de threads pour boutons/numpad
        if ignoreStartTimeout and not len(keyIn) and not keyData:
            return False
        
        if keyData != None:
            startTime = time()
            sleep_ms(100)
            keyIn += keyData
            if screenText:
                keyText = keyIn + '_' * (keyLength - len(keyIn))
                updateScreen(screenText, keyText)
        
        if len(keyIn) == keyLength:
            print("Keypad Value", keyIn)
            return keyIn
        
def getValidation():
    keyData = waitKeyPad(False, None, 1)
    if keyData != None:
        print("keyData", keyData)
        if not keyData in validationOption:
            print("Bad Validation Option")
            updateScreen("Mauvais choix", "A: Oui    B: Non")
        return keyData
    return False
    
def getKey():
    keyvalue = keyPad.scan()
    if keyvalue != None:
        print('Keypad input:', keyvalue)
        sleep_ms(200)
        return keyvalue