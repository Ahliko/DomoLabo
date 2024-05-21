from simple import MQTTClient
from BLEModule import BLE
from ventilo import Ventilo
import uasyncio as asyncio
import machine
from machine import Pin

button = machine.Pin(14, machine.Pin.IN, machine.Pin.PULL_UP)

async def main():
    
    while button.value():
        pass
    
    print("btn pressed")
    ble = BLE("DL Object")

    while (not ble.connect) or (not Ventilo.wifi_ssid or not Ventilo.wifi_password):
        pass

    print(Ventilo.wifi_ssid + "  :  " + Ventilo.wifi_password)

    ventilo = Ventilo()
    ventilo.main()

loop = asyncio.get_event_loop()
loop.run_until_complete(main())
