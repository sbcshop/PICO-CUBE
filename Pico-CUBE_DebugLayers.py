from machine import Pin
import time

# This code allows you to check an individual layer by setting LAYERTEST
# to the layer you want to test (see RESETLAYER for list of values).

LAYERTEST = 6  # Change this value to test different layers (9, 8, 7, 6)

LAYER = [LAYERTEST,LAYERTEST,LAYERTEST,LAYERTEST]
RESETLAYER = [9,8,7,6]

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
            
for pin in RESETLAYER:
    Pin(pin, Pin.IN)

for pin in LAYER:
    Pin(pin, Pin.OUT)

for x in range(4):
    for z in range(4):
        Pin(GRID_3D[x][z], Pin.IN)

for x in range(4):
    for z in range(4):
        Pin(GRID_3D[x][z], Pin.OUT)

reset(0)

for i in range(4):
        for j in range(4):
            light_on(i,i,j)
