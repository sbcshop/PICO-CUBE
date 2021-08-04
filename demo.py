from machine import Pin
import utime


LAYER = [9,8,7,6]

GRID_3D = [[16, 17, 1, 0],
     [18, 19, 3, 2],
     [20, 21, 5, 4],
     [22, 26, 27, 28]
     ]

def enable_layer(layer):
    a = Pin(LAYER[layer])
    a.on()

def disable_layer(layer):
    a = Pin(LAYER[layer])
    a.off()

def light_on(y, x, z):
    enable_layer(y)
    a = Pin(GRID_3D[x][z])
    a.on() 

def light_off(y, x, z):
    
    enable_layer(y)
    a = Pin(GRID_3D[x][z])
    a.off()
    

def reset():
    for x in range(4):
        for z in range(4):
            a = Pin(GRID_3D[x][z])
            a.off()
            utime.sleep(0.1)
            
def resetlayer():
    for i in range(0,4):
        a = Pin(LAYER[i])
        a.off()
        utime.sleep(0.01)

for pin in LAYER:
    Pin(pin, Pin.OUT)

for x in range(4):
    for z in range(4):
        Pin(GRID_3D[x][z], Pin.OUT)

        
reset()
resetlayer()

# Display each light in turn
for y in range(4):
    for x in range(4):
        for z in range(4):
            light_on(y, x, z)
            utime.sleep(0.1)
            light_off(y, x, z)
    disable_layer(y)

#Turn on all the lights
for y in range(4):
    enable_layer(y)
for x in range(4):
    for z in range(4):
        light_on(y, x, z)
        utime.sleep(0.25) 


