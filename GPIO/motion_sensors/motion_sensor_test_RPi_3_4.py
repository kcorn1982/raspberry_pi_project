from gpiozero import MotionSensor

pir = MotionSensor(4)

count = 0

while True:
    pir.wait_for_motion()
    print(f"You moved {count}")
    count += 1
    pir.wait_for_no_motion()
