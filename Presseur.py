from RFID_Payment import updateCardBalance
from I2C_Screen import updateScreen
from buzzer import createSound

from time import sleep_ms, time
from machine import PWM, Pin

button = Pin(19, Pin.IN, Pin.PULL_DOWN)

Red = PWM(Pin(16))
Green = PWM(Pin(17))
Blue = PWM(Pin(18))
Red.freq(1000)
Green.freq(1000)
Blue.freq(1000)

capacity = 0

def Presseur():    
    # Open Door
    
    updateScreen("Poser la canette", "Clic quand fini")
    buttonReclic = waitButton(60)
    if not buttonReclic:
        updateScreen("RETIRER MAINS", "DU PRESSEUR")
        createSound(50, 60)
        
        # Reclose Door
        print("Cancel Presseur")
        updateScreen("Action annulee", "Bonne journee !")
        sleep_ms(2500)
        return False
    
    # Close Door
    # Can => Poubelle
    
    addCountCapacity()
    
    updateScreen("Presenter Carte", "+10cts recyclage")
    paymentData = updateCardBalance('add', 10)
    if paymentData["status"] == False:
        print("Payment Cancel", paymentData["error"])
        updateScreen(paymentData["error"], "Bonne journée")
        createSound(3, 500)
        sleep_ms(1000)
        return False
    
    createSound(2, 50)
    newSoldeEuro = paymentData["balance"]/100
    print("Refund OK", f"newSolde {newSoldeEuro}")
    updateScreen("Remboursement OK", f"New Solde: {newSoldeEuro:2.2f}e")
    sleep_ms(2500)
    
    return True

#def pressCan():
    # Open Door
    # Wait reclic button
    # Close Door
    # Can => Poubelle
    # Add Count
    # Demander carte pour remboursement
    # Retour au début

def addCountCapacity():
    global capacity
    capacity += 1
    if capacity < 5:
        _RGB(0,255,0)
    elif capacity <= 7:
        _RGB(255,128,0)
    elif capacity >=10:
        _RGB(255,0,0)

def waitButton(timeout = 0):
    startTime = time()
    while True:
        sleep_ms(150)
        if timeout and (time() - startTime > timeout):
            return False
        
        if button.value():
            return True

def _RGB(r,g,b):
    Red.duty_u16(r*257)
    Green.duty_u16(g*257)
    Blue.duty_u16(b*257)
    
_RGB(0,255,0)