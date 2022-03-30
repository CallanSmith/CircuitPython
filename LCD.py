import board
from lcd.lcd import LCD
from lcd.i2c_pcf8574_interface import I2CPCF8574Interface
from digitalio import DigitalInOut, Direction, Pull
import time

# get and i2c object
i2c = board.I2C()

Button1 = DigitalInOut(board.D8)
Button1.direction = Direction.INPUT
Button1.pull = Pull.DOWN

Button2 = DigitalInOut(board.D9)
Button2.direction = Direction.INPUT
Button2.pull = Pull.DOWN

count = 0
callanGotIt = 1
switch = True
oldButton1 = Button1.value
oldButton2 = Button2.value


# some LCDs are 0x3f... some are 0x27.
lcd = LCD(I2CPCF8574Interface(i2c, 0x3f), num_rows=2, num_cols=16)


lcd.clear()

lcd.print("Presses")
lcd.set_cursor_pos(1,0)
lcd.print("SwitchState:UP  ") #Printing to the lcd the state of the switch


while True:
    button1 = Button1.value
    button2 = Button2.value
    
    # print(button1,"   ",oldButton1,"   ",button2,"   ",oldButton2 )
    # time.sleep(.05)
    

    
    if button1 and not oldButton1: #If Button 1 is pressed, and has been "unpressed"
        print("pressed!")
        count += callanGotIt # Varaiable representing 1
        lcd.set_cursor_pos(0,11) #Starting in the very first position
        lcd.print(str(count)) #Printing the number of presses to the lcd
        lcd.print("  ")   #Formatting to make the lcd printing and spacing look right
        

    if button2 and not oldButton2:
        switch = not switch # allows to turn button into switch
        print("switch") #Let me know on the serial monitor that the switch button has been pressed
        
        if switch:
            lcd.set_cursor_pos(1,0) # If "Switch" is on, print going up
            lcd.print("SwitchState:UP  ") #Printing to the lcd the state of the switch
            callanGotIt = 1
        else: # If "Switch" is off, print going down
            lcd.set_cursor_pos(1, 0)
            lcd.print("SwitchState:DOWN") #Printing to the lcd the state of the switch
            callanGotIt = -1

    oldButton1 = button1 #Allows you to hold button and it only goes up one
    oldButton2 = button2 #Allows button to turn into switch by staying with up or down value when pressed
    
