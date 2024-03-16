from actions import findActionObject, buyArticle, manageStocks
from I2C_Screen import updateScreen
# from Presseur import addCountCapacity
from keypad import waitKeyPad

from time import sleep_ms

from machine import Pin
from _thread import start_new_thread

# button = Pin(17, Pin.IN, Pin.PULL_DOWN)

def DistriPresseur():
    updateScreen("Selectionnez", "votre article...")
    
    actionCode = waitKeyPad(True, "Code produit")
    if not actionCode:
        print("Cancel Keypad")
        updateScreen("Action annulee", "Bonne journee !")
        sleep_ms(2500)
        return DistriPresseur()
    
    action = findActionObject(actionCode)
    if not action:
        print("Bad action", actionCode)
        updateScreen("Action inconnue", actionCode)
        sleep_ms(2500)
        return DistriPresseur()
    
    if action["type"] == "article":
        buyArticle(action)
    elif action["type"] == "manage_stocks":
        manageStocks()
     
    return DistriPresseur()

#def Presseur(_pin):
#    addCountCapacity()

#def ouioui():
#    print("vroum vroum")
#    sleep_ms(2500)
#    return ouioui()

DistriPresseur()
# start_new_thread(ouioui, ())
# button.irq(trigger=Pin.IRQ_RISING, handler=Presseur)


