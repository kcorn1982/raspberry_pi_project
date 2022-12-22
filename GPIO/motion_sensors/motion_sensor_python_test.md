# Python test for motion controller

Once you have connected your motion sensor you are going to want to test that is works.

Various scripts for different Pi's i've used are below.

## Python script for using a Raspberry Pi 3/4  

If you have cloned this repository you'll find the 
[motion_sensor_test_RPi_3_4.py](/GPIO/motion_sensors/motion_sensor_test_RPi_3_4.py) in this `motion_sensors` folder.

The code is below:

```python
from gpiozero import MotionSensor

pir = MotionSensor(4)

count = 0

while True:
    pir.wait_for_motion()
    print(f"You moved {count}")
    count += 1
    pir.wait_for_no_motion()

```
As you can see in the code above we have a simple while loop with a counter for each time the sensor detects movement.

Key points breakdown:

* [`gpiozero`](https://gpiozero.readthedocs.io/en/stable/) -> A simple package to help interface with GPIO devices.
* [`MotionSensor`](https://gpiozero.readthedocs.io/en/stable/api_input.html#motionsensor-d-sun-pir) -> Is one of the classes within the input devices section.
* `pir = MotionSensor(4)` -> The MotionSensor object expects a pin to be stated. This will be the GPIO pin you would have connected your motion sensor OUT pin.
* `pir.wait_for_motion()` -> This method pauses the script until motion is captured, when motion is captured it sends a 5v signal for a particular period to the GPIO pin.
* `pir.wait_for_no_motion()` -> Pause the script until the device is activated again, essentially waiting for the PIR sensor to start monitoring again.
