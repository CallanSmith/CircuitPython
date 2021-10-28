
# CircuitPython
 The follwing files are my first foray into CircuitPython.
## Table of Contents
* [Table of Contents](#TableOfContents)
* [Hello_CircuitPython](#Hello_CircuitPython)
* [CircuitPython_Servo](#CircuitPython_Servo)
* [CircuitPython_LCD](#CircuitPython_LCD)
* [NextAssignmentGoesHere](#NextAssignment)
---

## Hello_CircuitPython

### Description & Code

This assingment was to change the led of the metro board to different colors using dot.fill.

```python

while True:
    dot.fill((255,0,0))
    time.sleep(0.5)
    dot.fill((255,255,0))
    time.sleep(0.5)
    dot.fill((0,255,0))
    time.sleep(0.5)
    dot.fill((0,255,255))
    time.sleep(0.5)
    dot.fill((0,0,255))
    time.sleep(0.5)
    dot.fill((255,0,255))
    time.sleep(0.5)

```
The dot.fill code is what changes the color of the board, the values after are the specific color, and the time.sleep is the time inbetween the changing colors.

### Evidence

<img src="Blinkingboard.gif" alt="BlinkingBoard" width="450">
This image shows the led in the board changing colors.

[Credit to Quinn Ragsdale](https://github.com/qragsda80/CircuitPython1#evidence)

### Wiring

No Wiring for this assingment as it was just the board.

### Reflection

The hard part about this assingment was figuring out the different RGB values of the colors. I was able to find the values  on this  
[Website](https://www.w3schools.com/colors/colors_picker.asp)
This website gives all of the values you need for every specific color.

## CircuitPython_Servo

### Description & Code

This assingment was to use capacitive touch to change the direction of a turning servo.

```python

touch_pad1 = board.A0  
touch1 = touchio.TouchIn(touch_pad1)
touch_pad2 = board.A5  
touch2 = touchio.TouchIn(touch_pad2)

while True:

    if touch1.value:
        print("Touched the White Wire!")
        for angle in range(0, 180, 5):  # 0 - 180 degrees, 5 degrees at a time.
            my_servo.angle = angle
            time.sleep(0.05)
    if touch2.value:
        print("Touched the Green Wire!")
        for angle in range(180, 0, -5):  # 180 - 0 degrees, 5 degrees at a time
            my_servo.angle = angle
            time.sleep(0.05)
    time.sleep(0.05)
    print("end of loop!")

```
This is the meat of the code, it makes each wire a button and tells it which analog pin it is going into, it then prints "Touched the () wire" when that wire is touched.it then turns the servo one way or another which it -/+ 5

### Wiring

<img src="QuinnServoWiring.png" width="450">

[Credit to Quinn Ragsdale](https://github.com/qragsda80/CircuitPython1#evidence)

The two loose wires in this code stemming from A0 and A5 represent the two wires used for capacitive touch, there is also only 3 wires going to the servo in this wiring diagram but the servos we use require 4.

### Evidence
<img src="https://github.com/CallanSmith/CircuitPython/blob/main/Media/ServoGif.gif?raw=true" width="450">

This GIF shows the servo turning different directions when a different wire is toucheed. In this video it is a little confusing because I accedintaly touch two wires at once causing it to turn around prematurely.

### Reflection

The part  of this assingment that I struggled with was figuring out how to use capacitive touch. The key to capacitive touch is the touch1.value and using the library touchio. Once you have touch value set up you just have to set the angle range and direction using "for angle in range(0, 180, 5)" Switch 5 to -5 to turn other way





## CircuitPython_DistanceSensor

### Description & Code
This is the main two parts of the distance sensor code. The first part is using a function to have light on board fade and change colors. Since the math would be confusing if I used a function for the 20-35 part the better option was to use a map. That is the second part of the code mapping blue to green.

```python
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

```

### Evidence

<img src="ezgif.com-gif-maker.gif" alt="DistanceSesnorEvidence" width="450">

### Wiring
<img src="Distance sesnor wiring.png" alt="DistanceSesnorEvidence" width="450">

### Reflection
 This project taught how to use a function and how to map which will be important in the future. I struggled when figuring out the map because I had two functions and was saying the same things twice.
 
 ## CircuitPython_Photo_Interuptor
 
 ### Description & Code
This assingment was to use a photointeruptor to count the amount of times something was in it and print that to serial monitor.
```python
max = 4
start = time.monotonic()
while True:
    photo = interrupter.value
    if photo and not state:
            counter += 1
    state = photo

    remaining = max - time.monotonic()

    if remaining <= 0:
        print("Interrupts:", str(counter))
        max = time.monotonic() + 4
        counter = 0

```
[Link to code I used](https://github.com/gventre04/CircuitPython#photo-interrupter)
### Evidence
<img src="ezgif.com-gif-maker (1).gif" width="450">

### Wiring
<img src="IMG-3864.jpg" width="450">

### Reflection
 This assingments wiring was very simple and the code was't to bad, I just had to swtich time to time.monotonic
 
 ## 2.1 Designing the deck

### Description
 This was the first part of the skateboard design and it was very easy to complete

### Evidence
 <img src="Deck.png" alt="Deck" width="450">
 
 ### Reflection
This assingment was a good start but didnt teach me much.

 ## 2.2 Designing the Trucks

### Description
This was the second assingment, this was much harder. 
 ### Evidence
 <img src="Trucks.png" alt="Trucks" width="450">
 
 ### Reflection
 This assingment taught me a lot of things, including how to add new parts to one part studio
 
 ## 2.3 Designing the Wheels and bearings

### Description
 This assingment was easier and simple.
 
 ### Evidence
 <img src="Wheelsandbearings.png" alt="Wheelsandbearings" width="450">
 
 ### Reflection
 This assingment reminded me how to revolve correctly.
 
 ## 2.4 Assembly
 
 ### Description
 This was challnging and tedious but was made easier by things it taught me 
 
 ### Evidence
 <img src="Puttingitalltogether.png" alt="Assembly" width="450">
 
 ### Reflection
 This assingment taught me how to replicate screws and bolts I put in 
 
 ## 2.5 Lets Shred

### Description
 For this assingment I chose bending the board and inscribing a logo.
 
 ### Evidence
 <img src="LetsShred.png" alt="LetsShred" width="450">
 
 ### Reflection
 This assingment taught me how to bend flat objects.
 
 
 
 
 ## 3.2 One brick to rule them all
 

### Description
 The assingmet was to build use configurations to make the simple brick changlable into different shapes, rows/coloumns, and colors.

### Evidence
 
 <img src="3.2.png" alt="BrickConfig" width="450">
 
 ### Reflection
This assingmet taught me how to use configurations

 ## 3.1 How the pros do it.
 

### Description
 The assingmet was to build a simple 2x4 Lego brick using varaibales.

### Evidence
 
 <img src="3.1.png" alt="Assembly" width="450">
 
 ### Reflection
 This assingment taught me how to use a linear pattern
 
  ## 3.3 Putting it all toghether.
 

### Description
This assingment was to build some of the bricks together to make a bad lego duck

### Evidence
 <img src="3.3.png" alt="Duck" width="450">
 
 ### Reflection
 This assingment taught me how to use the snap tool which I thinkk willl be very usefull in the future

## 3.4 Drawing
 

### Description
This assingment was to make a detailed drawing of the duck assembly.

### Evidence
 <img src="3.4.png" alt="Drawing" width="450">
 
 ### Reflection
 This assingment taught me how make a drawing and explode which will both be helpfull in the future.

