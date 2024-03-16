from machine import PWM, Pin
from time import sleep_ms

Red = PWM(Pin(20))
Green = PWM(Pin(19))
Blue = PWM(Pin(18))
Red.freq(1000)
Green.freq(1000)
Blue.freq(1000)

capacity = 0

def addCountCapacity():
    global capacity
    capacity += 1
    print(capacity)
    if capacity < 5:
        RGB(0,255,0)
    elif capacity <= 7:
        RGB(255,128,0)
    elif capacity >=10:
        RGB(255,0,0)
        
def RGB(r,g,b):
    Red.duty_u16(r*257)
    Green.duty_u16(g*257)
    Blue.duty_u16(b*257)

RGB(0,255,0)