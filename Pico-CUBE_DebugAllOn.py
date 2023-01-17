from machine import Pin
import time

# Code to simply switch on the entire cube so that it's easy to see whether any
# LEDs aren't lighting up.

LAYER = [9,8,7,6]

GRID_3D = [[17, 16, 0, 1], 
           [19, 18, 2, 3],
           [21, 20, 4, 5],
           [26, 22, 28, 27]]

def enable_layer(layer):
    a = Pin(LAYER[layer])
    a.on()

def light_on(y,x,z):
    enable_layer(y)
    a = Pin(GRID_3D[x][z])
    a.on()
    
def reset(t):
    for x in range(4):
        for z in range(4):
            a = Pin(GRID_3D[x][z])
            a.off()
            time.sleep(t)
            
for pin in LAYER:
    Pin(pin, Pin.OUT)

for x in range(4):
    for z in range(4):
        Pin(GRID_3D[x][z], Pin.OUT)

reset(0)

for i in range(4):
        for j in range(4):
            light_on(i,i,j)
