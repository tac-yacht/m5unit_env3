from machine import I2C,Pin
from collections import namedtuple

from .sht30 import SHT30,TempHumiReadResult

class ENV3:
    def __init__(self, i2c: I2C = None, addr_sht: int = 0x44, addr_qmp: int = 0x70):
        if i2c is None:
            self.i2c = I2C(0, scl=Pin(15), sda=Pin(13))
        else:
            self.i2c = i2c
        self._sht = SHT30(self.i2c, addr_sht)

    def read_temp_and_humi(self) -> TempHumiReadResult:
        return self._sht.read()

    def read_temp(self) -> float:
        return self._sht.read().temperature

    def read_humi(self) -> float:
        return self._sht.read().humidity
