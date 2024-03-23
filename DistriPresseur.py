from actions import findActionObject, buyArticle, manageStocks
from Presseur import Presseur, waitButton
from I2C_Screen import updateScreen
from keypad import waitKeyPad

from time import sleep_ms
from _thread import start_new_thread

def DistriPresseur(notEnded = False):
    updateScreen("Selectionnez", "votre article...")
    actionCode = waitKeyPad(True, "Code produit", 3)
    
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

def PresseurBase():
    while True: 
        waitButton()
        
        print('vra')
        # Securité si autre partie déjà lancée
    
        Presseur()
        
        # Reset
        updateScreen("Selectionnez", "votre article...")

start_new_thread(PresseurBase, ())
DistriPresseur()



