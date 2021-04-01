# -*- coding: utf-8 -*-

import time
#import for mlx90614
import board
import busio as io
import adafruit_mlx90614

#import for pyrebase
import pyrebase

#import for max30102
import max30102
import hrcalc
#GPIO and smbus
import RPi.GPIO as GPIO
import smbus

#i2c conncetion for mlx90614
i2c = io.I2C(board.SCL, board.SDA, frequency=100000)
mlx = adafruit_mlx90614.MLX90614(i2c)

#initialization for max30102
m = max30102.MAX30102()

print(GPIO.getmode())
#Firebase config and initialization
firebaseConfig = {'apiKey': "AIzaSyCPSsqp5JC8gXKMr1MT0bQNWAc4m-fFNZQ",
    'authDomain': "thesis-9f92a.firebaseapp.com",
    'databaseURL': "https://thesis-9f92a-default-rtdb.firebaseio.com/",
    'projectId': "thesis-9f92a",
    'storageBucket': "thesis-9f92a.appspot.com",
    'messagingSenderId': "876388111768",
    'appId': "1:876388111768:web:cbeee00f863a9f6c4187ed",
    'measurementId': "G-TVM146RD3X"}

firebase = pyrebase.initialize_app(firebaseConfig)

db = firebase.database()

auth = firebase.auth()



#senosr runs

while True:
    #temperature
    objectString = "{:.2f}".format(mlx.object_temperature)
    objectCelsius = float(objectString)
    print("Object Temp: {} °C".format(objectString))

    db.child("sensor").child("user1").update(({"temperature": objectCelsius}))


    #oxygen and heartRate
    red, ir = m.read_sequential()
    result = hrcalc.calc_hr_and_spo2(ir[:100], red[:100])



    if(result[0]>0 and result[3]>0):
        print("hear_rate: {}".format(result[0]))
        print("oxygen_rate: {}".format(result[2]))
        db.child("sensor").child("user1").update(({'heart_rate': result[0], 'oxygen_level':result[3] }))


    time.sleep(2)

