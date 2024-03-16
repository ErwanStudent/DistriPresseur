from machine import Pin, SoftSPI
from mfrc522 import MFRC522
from time import time

sck = Pin(4, Pin.OUT)
copi = Pin(3, Pin.OUT) # Controller out, peripheral in
cipo = Pin(5, Pin.OUT) # Controller in, peripheral out
spi = SoftSPI(baudrate=100000, polarity=0, phase=0, sck=sck, mosi=copi, miso=cipo)
sda = Pin(2, Pin.OUT)
reader = MFRC522(spi, sda)
key = [0xFF, 0xFF, 0xFF, 0xFF, 0xFF, 0xFF]
option = 0
   
def updateCardBalance(actionType, amount):
    if actionType not in ['add', 'remove']:
        print('Action Type not valid')
        return False
    
    try:
        reader.init()
        startTime = time()

        while True:
            if time() - startTime > 30:
                return { "status": False, "error": "Delai depasse" }

            (status, _tag_type) = reader.request(reader.CARD_REQIDL)#Read the card type number
            if status == reader.OK:
                print('Find the card!')
                (status, raw_uid) = reader.anticoll()#Reads the card serial number of the selected card
                if status == reader.OK:
                    print('New Card Detected')
                    if reader.select_tag(raw_uid) == reader.OK:#Read card memory capacity
                        strCardBalance = reader.Read_Data(key, raw_uid)
                    
                        cardBalance = int(strCardBalance)
                        if actionType == 'remove':
                            if (amount > cardBalance):
                                print("Not enough balance")
                                return { "status": False, "error": "Solde insuffisant", "balance": cardBalance }
                            newBalance = cardBalance - amount
                        else:
                            newBalance = cardBalance + amount
                        
                        print('newBalance', newBalance)
                        reader.Write_Data(key, raw_uid, str(newBalance))
                        return { "status": True, "balance": newBalance }
    except Exception as error:
        print("An exception occurred:", error)
        return { "status": False, "error": "Erreur Interne" }
    
# updateCardBalance('add', 1000)