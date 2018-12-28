import ctypes
import time
import random




SendInput = ctypes.windll.user32.SendInput



#############################SF V Actions#############################
W = 0x11
A = 0x1E
S = 0x1F
D = 0x20
Z = 0x2C
# UP = 0xC8
# DOWN = 0xD0
# LEFT = 0xCB
# RIGHT = 0xCD
ENTER = 0x1C

light_kick = 0x30 #light kick
light_punch = 0x22 #light punch
medium_kick = 0x31 #medium kick
medium_punch = 0x23 #medium punch
heavy_kick = 0x32 #heavy kick
heavy_punch = 0x24 #heavy punch
all_kick = 0x33 #all kick
all_punch = 0x25 #all punch

def do_nothing():
    time.sleep(0.4)




# C struct redefinitions 
PUL = ctypes.POINTER(ctypes.c_ulong)
class KeyBdInput(ctypes.Structure):
    _fields_ = [("wVk", ctypes.c_ushort),
                ("wScan", ctypes.c_ushort),
                ("dwFlags", ctypes.c_ulong),
                ("time", ctypes.c_ulong),
                ("dwExtraInfo", PUL)]

class HardwareInput(ctypes.Structure):
    _fields_ = [("uMsg", ctypes.c_ulong),
                ("wParamL", ctypes.c_short),
                ("wParamH", ctypes.c_ushort)]

class MouseInput(ctypes.Structure):
    _fields_ = [("dx", ctypes.c_long),
                ("dy", ctypes.c_long),
                ("mouseData", ctypes.c_ulong),
                ("dwFlags", ctypes.c_ulong),
                ("time",ctypes.c_ulong),
                ("dwExtraInfo", PUL)]

class Input_I(ctypes.Union):
    _fields_ = [("ki", KeyBdInput),
                 ("mi", MouseInput),
                 ("hi", HardwareInput)]

class Input(ctypes.Structure):
    _fields_ = [("type", ctypes.c_ulong),
                ("ii", Input_I)]

# Actuals Functions

def pressKey(hexKeyCode):
    extra = ctypes.c_ulong(0)
    ii_ = Input_I()
    ii_.ki = KeyBdInput( 0, hexKeyCode, 0x0008, 0, ctypes.pointer(extra) )
    x = Input( ctypes.c_ulong(1), ii_ )
    ctypes.windll.user32.SendInput(1, ctypes.pointer(x), ctypes.sizeof(x))

def releaseKey(hexKeyCode):
    extra = ctypes.c_ulong(0)
    ii_ = Input_I()
    ii_.ki = KeyBdInput( 0, hexKeyCode, 0x0008 | 0x0002, 0, 
ctypes.pointer(extra) )
    x = Input( ctypes.c_ulong(1), ii_ )
    ctypes.windll.user32.SendInput(1, ctypes.pointer(x), ctypes.sizeof(x))

if __name__ == '__main__':
    time.sleep(8)
    while True:
        pressKey(D)
        time.sleep(0.05)
        pressKey(S)
        time.sleep(2)
        releaseKey(D) 
        releaseKey(S)

        time.sleep(1)