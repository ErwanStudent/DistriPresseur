from keypad_driver import KeyPad
from machine import Pin
import time

keyPad = KeyPad(13, 12, 11, 10, 9, 8, 7, 6)

def waitKeyPad():
    keyIn = ""
    while True:
        keydata = getKey()
        if keydata != None:
            time.sleep_ms(100)
            keyIn += keydata 
        
        if len(keyIn) == 3:
            print("Keypad Value", keyIn)
            return keyIn

def getKey():
    keyvalue = keyPad.scan()
    if keyvalue != None:
        print('Keypad input:', keyvalue)
        time.sleep_ms(200)
        return keyvalue
    
waitKeyPad()