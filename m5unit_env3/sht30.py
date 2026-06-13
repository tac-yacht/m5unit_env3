from machine import I2C
import time
from struct import unpack
from collections import namedtuple

TempHumiReadResult = namedtuple('TempHumiReadResult', ['temperature', 'humidity'])
RawReadResult = namedtuple('RawReadResult', ['temp_raw', 'temp_crc', 'humi_raw', 'humi_crc'])

class SHT30:
    def __init__(self, i2c: I2C, address: int = 0x44):
        self.i2c = i2c
        self.address = address

    def read_raw(self) -> RawReadResult:
        self.i2c.writeto(self.address, bytearray([0x24,0x00]))
        time.sleep_ms(20)
        data = self.i2c.readfrom(self.address, 6)
        return RawReadResult(*unpack('>HBHB', data))

    def read(self) -> TempHumiReadResult:
        raw = self.read_raw()
        temp = -45 + 175 * (raw.temp_raw / 65535 )
        humi = 100 * (raw.humi_raw /65535 )
        return TempHumiReadResult(temp, humi)
