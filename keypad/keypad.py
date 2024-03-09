from keypad_driver import KeyPad
from I2C_Screen import updateScreen
from time import time, sleep_ms

keyPad = KeyPad(13, 12, 11, 10, 9, 8, 7, 6)

validationOption = ["A", "B"]

def waitKeyPad(ignoreStartTimeout = False, screenText = None, keyLength = 3):
    keyIn = ""
    startTime = time()
    while True:
        if ((not ignoreStartTimeout) or len(keyIn)) and (time() - startTime > 30):
            return False
        
        keyData = getKey()
        if keyData != None:
            startTime = time()
            sleep_ms(100)
            keyIn += keyData
            if screenText:
                updateScreen(screenText, keyIn)
        
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