from I2C_Screen import updateScreen
from keypad import waitKeyPad

articles = [
    { "code": "001", "name": "Coca Cola", "price": 100 },
    { "code": "002", "name": "Perrier", "price": 50 },
    { "code": "003", "name": "Orangina", "price": 130 },
]

def DistriPresseur():
    updateScreen("  Selectionnez", "votre article...")
    
    articleCode = waitKeypad()
    print("articleCode")
    
    article = findArticleObject(articleCode)
    if not article:
        print("Bad article", articleCode)
        updateScreen("Article inconnu", articleCode)
        # Mettre sleep 2s
        # return DistriPresseur()
    
    
    
def findArticleObject(code):
    for x in articles:
        if x["code"] == code:
            return x
    return False

DistriPresseur()