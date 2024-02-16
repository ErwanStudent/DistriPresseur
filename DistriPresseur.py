from keypad import waitKeyPad, getValidation
from RFID_Payment import updateCardBalance
from I2C_Screen import updateScreen
import time

articles = [
    { "code": "001", "name": "Coca Cola", "price": 100 },
    { "code": "002", "name": "Perrier", "price": 50 },
    { "code": "003", "name": "Orangina", "price": 130 },
]

def DistriPresseur():
    updateScreen("  Selectionnez", "votre article...")
    
    articleCode = waitKeyPad()
    article = findArticleObject(articleCode)
    if not article:
        print("Bad article", articleCode)
        updateScreen("Article inconnu", "      " + articleCode)
        time.sleep_ms(2500)
        return DistriPresseur()
    
    priceEuro = article["price"]/100
    articleDisplay = f"{article["name"]} - {priceEuro:2.2f}e"[:16]
    updateScreen(articleDisplay, "A: Oui    B: Non")
    
    validationKey = getValidation()
    if validationKey == "B":
        print("Cancel")
        updateScreen("  Achat annule", "Bonne journee !")
        time.sleep_ms(2500)
        return DistriPresseur()
    
    updateScreen("Presenter Carte", articleDisplay)
    paymentData = updateCardBalance("remove", article["price"])
    if paymentData["status"] == False:
        print("Payment Cancel", paymentData["error"])
        updateScreen(paymentData["error"], "Ressayer + tard")
        time.sleep_ms(2500)
        return DistriPresseur()
    
    newSoldeEuro = paymentData["balance"]/100
    print("Payment OK", f"newSolde {newSoldeEuro}")
    updateScreen("Paiement OK", f"New Solde: {newSoldeEuro}e"[:16])
    time.sleep_ms(2500)
    
    return DistriPresseur()
    
def findArticleObject(code):
    for x in articles:
        if x["code"] == code:
            return x
    return False

DistriPresseur()