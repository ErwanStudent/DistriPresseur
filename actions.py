from keypad import getValidation, waitKeyPad
from RFID_Payment import updateCardBalance
from I2C_Screen import updateScreen
from buzzer import createSound

from time import time, sleep_ms

actions = [
    { "type": "article", "code": "001", "name": "Coca Cola", "price": 100, "stock": 3 },
    { "type": "article", "code": "002", "name": "Perrier", "price": 50, "stock": 3 },
    { "type": "article", "code": "003", "name": "Orangina", "price": 130, "stock": 3 },
    
    { "type": "manage_stocks", "code": "123" },
]

def buyArticle(article):
    if article["stock"] == 0:
        print("No enough stock", article["name"])
        updateScreen("Plus de stock", article["name"])
        sleep_ms(2500)
        return False
    
    priceEuro = article["price"]/100
    articleDisplay = f"{article["name"]} - {priceEuro:2.2f}e"
    updateScreen(articleDisplay, "A: Oui    B: Non")
    
    validationKey = getValidation()
    if validationKey != "A":
        print("Cancel")
        updateScreen("Achat annule", "Bonne journee !")
        sleep_ms(2500)
        return False
    
    updateScreen("Presenter Carte", articleDisplay)
    paymentData = updateCardBalance("remove", article["price"])
    if paymentData["status"] == False:
        print("Payment Cancel", paymentData["error"])
        updateScreen(paymentData["error"], "Ressayer + tard")
        createSound(3, 500)
        sleep_ms(1000)
        return False
    
    createSound(2, 50)
    newSoldeEuro = paymentData["balance"]/100
    print("Payment OK", f"newSolde {newSoldeEuro}", article["name"])
    updateScreen("Paiement OK", f"New Solde: {newSoldeEuro}e")
    sleep_ms(2500)
    
    # Remove article in stock
    article["stock"] = article["stock"] - 1
    
    return True

def manageStocks():
    updateScreen("Code de", "votre article ?")
    articleCode = waitKeyPad(True)
    if not articleCode:
        print("Cancel Keypad ManageStocks")
        updateScreen("Action annulee", "Bonne journee !")
        sleep_ms(2500)
        return False
    
    article = findActionObject(articleCode)
    if not article or article["type"] != "article":
        print("Not a article", articleCode, article)
        updateScreen("Pas un article", articleCode)
        sleep_ms(2500)
        return manageStocks()
    
    
    
def findActionObject(code):
    for action in actions:
        if action["code"] == code:
            return action
    return False