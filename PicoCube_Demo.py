from machine import Pin
import time
import random

LAYER = [9,8,7,6]#layers

#columns
GRID_3D = [[17, 16, 0, 1], 
           [19, 18, 2, 3],
           [21, 20, 4, 5],
           [26, 22, 28, 27]]


def enable_layer(layer):
    a = Pin(LAYER[layer])
    a.on()

def disable_layer(layer):
    a = Pin(LAYER[layer])
    a.off()

def light_on(y,x, z,):
    enable_layer(y)
    a = Pin(GRID_3D[x][z])
    a.on()
    
def light_off(y, x, z):
    enable_layer(y)
    a = Pin(GRID_3D[x][z])
    a.off()
    

def reset(t):
    for x in range(4):
        for z in range(4):
            a = Pin(GRID_3D[x][z])
            a.off()
            time.sleep(t)
            
def resetlayer():
    for i in range(0,4):
        a = Pin(LAYER[i])
        a.off()
        time.sleep(0.01)

for pin in LAYER:
    Pin(pin, Pin.OUT)

for x in range(4):
    for z in range(4):
        Pin(GRID_3D[x][z], Pin.OUT)



while 1:

    for i in range(4):
            for j in range(4):
                light_on(i,i,j)
                time.sleep(0.1)
    reset(0)
        
    for i in reversed(range(4)):
            for j in reversed(range(4)):
                light_on(i,i,j)
                time.sleep(0.1)
    reset(0)



