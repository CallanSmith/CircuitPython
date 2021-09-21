import time
import board
import neopixel
import adafruit_hcsr04
import simpleio

sonar = adafruit_hcsr04.HCSR04(trigger_pin=board.D2, echo_pin=board.D3)
dot = neopixel.NeoPixel(board.NEOPIXEL, 1)
distance = 0

while True:
    try:
        distance = sonar.distance
        print((distance,))

        if distance < 5:
            print("red")
            dot.fill((255, 0, 0))
        elif distance <= 20:
            r = 255-((distance-5)/15*255)
            g = 0
            b = (distance-5)/15*255
            dot.fill((int(r), int(g), int(b)))
        else:
            # Had two else statements which isn't allowed,
            # had unnecesary funciton which conjumbled code
            # didnt have necesary library for mapped function
            r = 0
            g = simpleio.map_range(distance, 20, 35, 0, 255)  #had two things saying the same thins which made my code a mess
            b = simpleio.map_range(distance, 20, 35, 255, 0)
            dot.fill((int(r), int(g), int(b)))
    except RuntimeError:
        print("Retrying!")
        pass
        time.sleep(0.1)


# r = 0
# b = simpleio.map_range(distance, 20, 35, 255, 0)
# g = simpleio.map_range(distance, 20, 35, 0, 255)
