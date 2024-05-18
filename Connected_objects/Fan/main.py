from simple import MQTTClient
from BLEModule import BLE
from ventilo import Ventilo
import uasyncio as asyncio

async def main():
    ble = BLE("DL Object")

    while (not ble.connect) or (not Ventilo.wifi_ssid or not Ventilo.wifi_password):
        pass

    print(Ventilo.wifi_ssid + "  :  " + Ventilo.wifi_password)
    
    ventilo = Ventilo()
    ventilo.main()

loop = asyncio.get_event_loop()
loop.run_until_complete(main())