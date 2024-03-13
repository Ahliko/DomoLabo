from time import sleep_ms
import ubluetooth
import network
import uasyncio as asyncio

wlan_sta = network.WLAN(network.STA_IF)
wlan_sta.active(True)

wlan_mac = wlan_sta.config('mac')


class BLE:
    def __init__(self, name):

        self.service_uuid = "3a13c4ec-4e06-49a2-8fa2-e189f0a9364a"
        self.characteristic_uuid = "fd3b1289-4226-41fa-abe4-d9b6066a5b20"
        self.description_uuid = "d9f4578a-ce79-47ec-aab8-c1c0c4fac959"

        self.name = "0df0032e|" + name

        self.ble = ubluetooth.BLE()
        self.ble.active(True)
        self.connect = False

        self.d = "mytopicObject"

        self.disconnected()
        self.ble.irq(self.ble_irq)
        self.register()
        self.advertiser()

    def connected(self):
        print('connected')
        self.connect = True

    def disconnected(self):
        sleep_ms(200)
        self.connect = False

    def ble_irq(self, event, data):
        if event == 1:
            '''Central disconnected'''
            self.connected()

        elif event == 2:
            '''Central disconnected'''
            print("deconnect")
            self.advertiser()
            self.disconnected()

        elif event == 3:
            '''New message received'''
            buffer = self.ble.gatts_read(self.rx)
            message = buffer.decode('UTF-8').strip()
            print(message)

    def register(self):

        ble_service_uuid = ubluetooth.UUID(self.service_uuid)

        ble_characteristic = (ubluetooth.UUID(self.characteristic_uuid), ubluetooth.FLAG_WRITE | ubluetooth.FLAG_READ)

        ble_service1 = (ble_service_uuid, (ble_characteristic,))

        ble_services = (ble_service1,)


        ((self.t,),) = self.ble.gatts_register_services(ble_services)
        self.ble.gatts_write(self.t, self.d.encode())



    async def send(self, data):
        print(f"send {data}")
        self.ble.gatts_notify(0, self.tx, data + '\n')
        await asyncio.sleep(0.1)

    def advertiser(self):
        name = bytes(self.name, 'UTF-8')
        self.ble.gap_advertise(500000, bytearray(b'\x02\x01\x02') + bytearray([len(name) + 1, 0x09]) + name)


async def main():
    ble = BLE("DL Object")

    while not ble.connect:
        pass

    while ble.connect:
        pass


# Run the main coroutine
loop = asyncio.get_event_loop()
loop.run_until_complete(main())
