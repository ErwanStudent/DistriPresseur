from machine import Pin, PWM
import utime

pwmPin = 20
cwPin = 21
acwPin = 22

def motorMove(speed, direction, speedGP, cwGP, acwGP):
    if speed > 100: speed=100
    if speed < 0: speed=0
    Speed = PWM(Pin(speedGP))
    Speed.freq(50)
    cw = Pin(cwGP, Pin.OUT)
    acw = Pin(acwGP, Pin.OUT)
    Speed.duty_u16(int(speed/100*65536))
    if direction < 0:
        cw.value(0)
        acw.value(1)
    if direction == 0:
        cw.value(0)
        acw.value(0)
    if direction > 0:
        cw.value(1)
        acw.value(0)

def upMotor():
    motorMove(100,-1, pwmPin, cwPin, acwPin)
    utime.sleep(5)
    
def downMotor():
    motorMove(100,1, pwmPin, cwPin, acwPin)
    utime.sleep(5)
    
upMotor()