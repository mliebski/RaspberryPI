import smbus
from time import *

class i2c_device:
        def __init__(self, addr, port=1):
                self.addr=addr
                self.bus=smbus.SMBus(port)

        #write a single command
        def write_cmd(self, cmd):
                self.bus.write_byte(self.addr, cmd)
                sleep(0.0001)

        #write a command and an argument
        def write_cmd_arg(self, cmd, data):
                self.bus.write_byte_data(self.addr, cmd, data)
                sleep(0.0001)

        #write a block of data
        def write_block_of_data(self, cmd, data):
                self.bus.write_block_data(self.addr, cmd, data)
                sleep(0.0001)

        # read a single byte
        def read(self):
                return self.bus.read_byte(self.addr)

        #Read
        def read_data(self, cmd):
                return self.bus.read_byte_data(self.addr, cmd)

        #read a block of data
        def read_block_data(self, cmd):
                return self.bus.read_block_data(self.addr, cmd)
