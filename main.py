"""
Buttons - User interface
# 6  = Set_Alarm 
# 7 = add minutes/hours
# 8 = substract minutes/hoursSet_Minutes 
# 9 = Confirm / Disable alarm

"""

####################Import all the libraries#######################
from machine import I2C, Pin
from ds1302 import DS1302
from pico_i2c_lcd import I2cLcd
import utime
###################################################################


################Setup LCD I2C and initialize#######################
I2C_ADDR     = 39
I2C_NUM_ROWS = 2
I2C_NUM_COLS = 16

i2c = I2C(0, sda=machine.Pin(0), scl=machine.Pin(1), freq=400000)
lcd = I2cLcd(i2c, I2C_ADDR, I2C_NUM_ROWS, I2C_NUM_COLS)
lcd.backlight_on()
###################################################################


################Setup DS1302 and initialize###########################
ds = DS1302(Pin(18),Pin(17),Pin(16))
ds.date_time() # returns the current datetime.
ds.date_time([2024, 11, 25, 0, 12, 42, 0]) # set datetime. comment out
print(ds.date_time())

print(ds.date_time())
print(ds.date_time())
######################################################################


#################initialize the Buzzer################################
buzzer = Pin(14, Pin.OUT)
buzzer.low()
######################################################################





#################Buttons#############################################
Button_pins = [6,7,8,9]

Button = []
# Loop to assign GPIO pins and setup input and outputs
for x in range(0,4):

    Button.append(Pin(Button_pins[x], Pin.IN, Pin.PULL_DOWN))
    Button[x].value(0)
######################################################################
    
    
#################Set initial values of alarm############################################# 
set_hour = 25
set_minute = 3
set_second = 00
hour = 0
minute = 0
#########################################################################################    
    

def set_alarm():
    
    global set_hour
    global set_minute
    global set_second
    global hour
    global minute
    
    lcd.clear()
    lcd.move_to(0,0)
    lcd.putstr("Set hour:")
    
    while Button[3].value() != 1:    
        if Button[1].value() == 1:
            set_hour += 1
            utime.sleep(0.1)
            set_hour = set_hour%24
            
        elif Button[2].value() == 1:
            set_hour -= 1
            utime.sleep(0.1)
            set_hour = set_hour%24
            
        hour = str(set_hour)
        
        while len(hour) < 2:
            hour = '0' + hour
        
        lcd.move_to(10,0)
        lcd.putstr(str(hour))
        
    lcd.clear()
    utime.sleep(0.3)
    lcd.move_to(0,0)
    lcd.putstr("Set minute:")
    
    while Button[3].value() != 1:
        if Button[1].value() == 1:
            set_minute += 1
            utime.sleep(0.1)
            set_minute = set_minute%60
        
        elif Button[2].value() == 1:
            set_minute -= 1
            utime.sleep(0.1)
            set_minute = set_minute%60
        
        minute = str(set_minute)
        while len(minute) < 2:
            minute = '0' + minute
            
        lcd.move_to(12,0)
        lcd.putstr(str(minute))
    
    lcd.clear()
    
    return(set_hour,set_minute)
        
    
def check_alarm(set_hour,set_minute,set_second):
    print("Check Alarm")
    if set_hour == int(hr) and set_minute == int(m) and set_second == int(s) :

        while Button[3].value() != 1:
            lcd.clear()
            lcd.move_to(4,0)
            print("Wake Up --------------------------------------------------------------------------")
            lcd.putstr("Wake Up!")
        
            utime.sleep(0.1)
            buzzer.low()
            utime.sleep(0.1)
            buzzer.high()
            lcd.clear()
    buzzer.low()


utime.sleep(1)        

### Welcome Message ###           
lcd.move_to(0,0)
lcd.putstr("Pico Alarm Clock")
lcd.move_to(0,1)
lcd.putstr("  Angelo/Pat   ")
utime.sleep(4)
lcd.clear()

while True:
    
    
    
    (Y,M,D,day,hr,m,s)=ds.date_time()
    if s < 10:
        s = "0" + str(s)
    if m < 10:
        m = "0" + str(m)
    if hr < 10:
        hr = "0" + str(hr)
    if D < 10:
        D = "0" + str(D)
    if M < 10:
        M = "0" + str(M)
        
    lcd.move_to(0,0)
    lcd.putstr("Time:")
    lcd.move_to(6,0)
    lcd.putstr(str(hr) + ":" + str(m) + ":" + str(s))
    lcd.move_to(0,1)
    lcd.putstr("Date:")
    lcd.move_to(6,1)
    lcd.putstr(str(D) + "/" + str(M) + "/" + str(Y))
    
    
    if Button[0].value() == 1:
        utime.sleep(0.1)
        print("Set Alarm")
        set_alarm()
    
 
    check_alarm(set_hour,set_minute,set_second)
             