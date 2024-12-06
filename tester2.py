from machine import I2C, Pin
from pico_i2c_lcd import I2cLcd

I2C_ADDR = 39  # Update with the correct I2C address
I2C_NUM_ROWS = 2
I2C_NUM_COLS = 16

i2c = I2C(0, sda=Pin(0), scl=Pin(1), freq=400000)
lcd = I2cLcd(i2c, I2C_ADDR, I2C_NUM_ROWS, I2C_NUM_COLS)
lcd.backlight_on()
lcd.putstr("Hello, World!")
