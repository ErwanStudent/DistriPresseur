from machine import Pin, SoftSPI
from mfrc522 import MFRC522

sck = Pin(2, Pin.OUT)
copi = Pin(3, Pin.OUT) # Controller out, peripheral in
cipo = Pin(4, Pin.OUT) # Controller in, peripheral out
spi = SoftSPI(baudrate=100000, polarity=0, phase=0, sck=sck, mosi=copi, miso=cipo)
sda = Pin(5, Pin.OUT)
reader = MFRC522(spi, sda)
key = [0xFF, 0xFF, 0xFF, 0xFF, 0xFF, 0xFF]
option = 0
   
def UpdateCardBalance(actionType, amount):
    if actionType not in ['add', 'remove']:
        print('Action Type not valid')
        return False
    
    try:
        while True:
            (status, tag_type) = reader.request(reader.CARD_REQIDL)#Read the card type number
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
                                return False
                            newBalance = cardBalance - amount
                        else:
                            newBalance = cardBalance + amount
                        
                        print('newBalance', newBalance)
                        reader.Write_Data(key, raw_uid, str(newBalance))
                        return True
    except Exception as error:
        print("An exception occurred:", error)
        return False
                
UpdateCardBalance('remove', 150)