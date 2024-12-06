from machine import Pin, I2C

i2c = I2C(0, sda=Pin(0), scl=Pin(1))
devices = i2c.scan()

if devices:
    print("I2C devices found:", devices)
else:
    print("No I2C devices found")