from actions import findActionObject, buyArticle, manageStocks
from I2C_Screen import updateScreen
from keypad import waitKeyPad

from time import sleep_ms

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

DistriPresseur()