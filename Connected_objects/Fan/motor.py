from machine import Pin, PWM

class Motor:
    def __init__(self, pin1, pin2):
        self.pin1 = Pin(pin1, Pin.OUT)
        self.pin2 = Pin(pin2, Pin.OUT)
        self.pin1.value(0)
        self.pin2.value(0)
        self.vitesse = 50
        self.speed = PWM(Pin(pin1))
        self.speed.freq(self.vitesse)
        self.stopBlock()

    def start(self, vitesse):
        self.speed.duty(int((vitesse / 100) * 1023))
        self.pin1.value(1)
        self.pin2.value(0)
        if vitesse == 0 :
            self.stopBlock()


    def stopBlock(self):
        print("sblock")
        self.speed.duty(int((0 / 100) * 1023))
        self.pin1.value(1)
        self.pin2.value(1)


