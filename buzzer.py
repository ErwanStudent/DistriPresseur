from machine import Pin
from time import sleep_ms

buzzer = Pin(28, Pin.OUT)

def createSound(frequency, delay_ms):
    for i in range(frequency):
        time = i + 1
        print(f"createSound - {time}/{frequency}")
        buzzer.value(1)
        sleep_ms(delay_ms)
        buzzer.value(0)
        sleep_ms(delay_ms)