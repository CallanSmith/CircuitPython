# These are the libraries needed to fade an LED, even if you imported elsewhere
import time
import board
import pwmio
import digitalio

lightBulb = digitalio.DigitalInOut(board.D13)       # I moved my RGBLED power wire from 5v
lightBulb.direction = digitalio.Direction.OUTPUT    # and plugged it into D13.  I'll explain later.

class LED:      # It's propper coding to always write a line explaining a class
                # with a "docstring."   Like this:
    '''LED is a class designed for a single color LED to fade in and out'''

    def __init__(self, ledpin, name):
        # init is like void Setup() from arduino.  Initialize your pins here
        # self.led = pwmio.PWMOut(ledpin, frequency=5000, duty_cycle=0)
        self.name = name
        self.led = pwmio.PWMOut(ledpin, frequency=5000, duty_cycle=65535)#create a pulseio object called "mred" using pin "red" with a frequency of 5,000 Hz and a 16-bit integer which is a fraction that represents how much of one cycle is high or low


    def fadedown(self): # Fades LED from bright to dim
        for i in range(255):
            if i < (255/2):
                self.led.duty_cycle = int(i * 65535 / (255/2))
            print(self.led, "mgreen, mblue", self.led.duty_cycle)
            time.sleep(0.01)

    def fadeup(self):  # Fades LED from dim to bright
        for i in range(255):
            if i > (255/2):
                self.led.duty_cycle = 65535 - int((i - (255/2)) * 65535 / (255/2))
            print(self.led, "mgreen, mblue", self.led.duty_cycle)
            time.sleep(0.01)

    def on(self, brightness=65535):  # Remember "on" means duty cycles < 65535
        self.led.duty_cycle = 65535 - brightness
        lightBulb.value = 65535

    def off(self): # "off" means duty cycle should be full.
        self.led.duty_cycle = 65535


class RGB:
    '''this class should impliment all 3 pins together to control an RGB LED'''
    from rgb import LED
        # Let's take a second to appreciate that we're using a class to call a class!
        # Let LED do all the nitty gritty work, this RGB class will be the "manager"

    def __init__(self, redPin, greenPin, bluePin):
        # To initialize an RGB LED, we need to initialize 3 LED pins.
        self.myRedLED = LED(redPin, "red")
        self.myBlueLED = LED(bluePin, "blue")
        self.myGreenLED = LED(greenPin, "green")

    def blue(self, brightness=65535):
        # Notice the brightness=65535?  Thats an OPTIONAL parameter!  So in main.py,
        # you can call "RGBLED1.blue() for full brightness, or "RGBLED1.blue(half) to
        # make it dimmer!
        self.myBlueLED.on(brightness)
        self.myGreenLED.off()
        self.myRedLED.off()

    def red(self, brightness=65535):
        self.myBlueLED.off()
        self.myGreenLED.off()
        self.myRedLED.on(brightness)

    def green(self, brightness=65535):

        self.myBlueLED.off()
        self.myGreenLED.on(brightness)
        self.myRedLED.off()

    def cyan(self, brightness=65535):
        # Notice the brightness=65535?  Thats an OPTIONAL parameter!  So in main.py,
        # you can call "RGBLED1.blue() for full brightness, or "RGBLED1.blue(half) to
        # make it dimmer!
        self.myBlueLED.on(brightness / 2)
        self.myGreenLED.on(brightness / 2)
        self.myRedLED.on(brightness)

    def magenta(self, brightness=65535):
        # Notice the brightness=65535?  Thats an OPTIONAL parameter!  So in main.py,
        # you can call "RGBLED1.blue() for full brightness, or "RGBLED1.blue(half) to
        # make it dimmer!
        self.myBlueLED.on(brightness)
        self.myGreenLED.on(brightness / 2)
        self.myRedLED.on(brightness / 2)# Write a bunch
    # of more methods
    # here.

    def off(self):
        # This turns off all 3 LEDs, but my LEDs were still glowing a tiny bit.
        # To fix this, i took the RGB power wire out of 5V , and plugged it into D13.
        # Now when I want the LED to be off, it's truly off!
        self.myBlueLED.off()
        self.myGreenLED.off()
        self.myRedLED.off()
        lightBulb.value = 0