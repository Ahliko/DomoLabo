from machine import Pin, PWM

class Motor:

    def __init__(self, pin1, pin2):
        self.pin1 = Pin(pin1, Pin.OUT)
        self.pin2 = Pin(pin2, Pin.OUT)
        self.pin1.value(1)
        self.pin2.value(1)
        self.vitesse = 1000
        self.speed = PWM(Pin(pin1))
        self.speed.freq(self.vitesse)

    def start(self, vitesse):
        self.speed.duty(int((vitesse / 100) * 1024))
        self.pin2.value(0)

    def stopBlock(self):
        self.pin1.value(1)
        self.pin2.value(1)

    def stopLibre(self):
        self.pin1.value(0)
        self.pin2.value(0)