from keypad_driver import KeyPad
from I2C_Screen import updateScreen
import time

keyPad = KeyPad(13, 12, 11, 10, 9, 8, 7, 6)

validationOption = ["A", "B"]

def waitKeyPad():
    keyIn = ""
    while True:
        keyData = getKey()
        if keyData != None:
            time.sleep_ms(100)
            keyIn += keyData
            updateScreen("Code produit", keyIn)
        
        if len(keyIn) == 3:
            print("Keypad Value", keyIn)
            return keyIn
        
def getValidation():
    while True:
        keyData = getKey()
        if keyData != None:
            print("keyData", keyData)
            if not keyData in validationOption:
                print("Bad Validation Option")
                updateScreen("Mauvais choix", "A: Oui    B: Non")
                return getValidation()
    
            return keyData 
    


def getKey():
    keyvalue = keyPad.scan()
    if keyvalue != None:
        print('Keypad input:', keyvalue)
        time.sleep_ms(200)
        return keyvalue