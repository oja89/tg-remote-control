"""
controls Hue Smart Plug with bluetooth using bleak

Source:
https://github.com/aroidzap/philips-hue-ble/blob/main/hue.py
Copyright (c) 2023 Tomáš Pazdiora
"""

import asyncio
from bleak import BleakClient, BleakScanner

class HueScanner(BleakScanner):
    SERVICE_UUID = '0000fe0f-0000-1000-8000-00805f9b34fb'
    def __init__(self):
        super().__init__(service_uuids=[HueScanner.SERVICE_UUID])


class HueClient(BleakClient):   

    def _command(command):
        """
        Fill the needed code around the command
        """
        return '932c32bd-'+ str(command).zfill(4) + '-47a2-835a-a8d455b859dd'

    def __init__(self, ble_address):
        super().__init__(ble_address)

    async def get_power(self):
        """
        Gets power state (True == on, False == off)
        """
        resp = await self.read_gatt_char(HueClient._command(2))
        return bool(resp == b'\x01')
    
    async def set_power(self, enabled):
        """
        Sets power state (True == on, False == off)
        """
        data = b'\x01' if enabled else b'\x00'
        #return await self.write_gatt_char(HueClient._command(2), data, response=True)
        # check status before and after
        before = await self.get_power()
        await self.write_gatt_char(HueClient._command(2), data, response=True)
        after = await self.get_power()
        return (str(before) + str(after))
        

async def main(address = None):
    if address is None:
        print("BLE Scanning...")
        print()

        hue_devices = await HueScanner.discover()
        hue_devices = sorted(hue_devices, key=lambda d: d.rssi, reverse=True)
        
        # this finds more than just the hue devices, but tests only the first
        print(hue_devices)
        
        device = hue_devices[0]

        address = device.address
        print(f"BLE Device: {device.name}")
        print(f"BLE rssi: {device.rssi}")
    
    print()
    print(f"BLE Address: {address}")

    async with HueClient(address) as hue:
        print(f"BLE connected: {hue.is_connected}")

        print(f"Power: {await hue.get_power()}")
        await asyncio.sleep(0.5)

        print(f"Switch on: {await hue.set_power(True)}")
        await asyncio.sleep(0.5)
                
        print(f"Power: {await hue.get_power()}")
        await asyncio.sleep(0.5)
                
        print(f"Switch off: {await hue.set_power(False)}")
        await asyncio.sleep(0.5)

        print(f"Power: {await hue.get_power()}")
        await asyncio.sleep(0.5)

if __name__ == "__main__":
    asyncio.run(main())
