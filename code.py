import RPi.GPIO as GPIO
2 import time
3
4 IR_SENSOR = 17
5 LED = 27
6 SERVO = 18
7
8 GPIO.setmode(GPIO.BCM)
9 GPIO.setup(IR_SENSOR, GPIO.IN)
10 GPIO.setup(LED, GPIO.OUT)
11 GPIO.setup(SERVO, GPIO.OUT)
12
13 pwm = GPIO.PWM(SERVO, 50)
14 pwm.start(0)
15
16 def set_angle(angle):
17 duty = 2 + (angle / 18)
18 GPIO.output(SERVO, True)
19 pwm.ChangeDutyCycle(duty)
20 time.sleep(0.5)
21 GPIO.output(SERVO, False)
22 pwm.ChangeDutyCycle(0)
23
24 while True:
25 if GPIO.input(IR_SENSOR):
26 GPIO.output(LED, True)
27 set_angle(90)
28 else:
29 GPIO.output(LED, False)
30 set_angle(0)