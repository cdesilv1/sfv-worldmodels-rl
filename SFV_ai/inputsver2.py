import ctypes
import time
import random




SendInput = ctypes.windll.user32.SendInput



#############################SF V Actions#############################

#############################Movement#############################
UP = 0x11 #W
LEFT = 0x1E #A
DOWN = 0x1F #S
RIGHT = 0x20 #D

UP_LEFT = [UP, LEFT]
UP_RIGHT = [UP, RIGHT]
DOWN_LEFT = [DOWN, LEFT]
DOWN_RIGHT = [DOWN, RIGHT]



#############################Basic Attacks#############################

LK = 0x30 #light kick
LP = 0x22 #light punch
MK = 0x31 #medium kick
MP = 0x23 #medium punch
HK = 0x32 #heavy kick
HP = 0x24 #heavy punch
AK = 0x33 #all kick
AP = 0x25 #all punch



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



def executeAction(action, duration=0.05):
    if type(action) is int:
        pressKey(action)
        time.sleep(duration)
        releaseKey(action)

    elif type(action) is list:
        for i in range(len(action)):
            pressKey(action[i])
        time.sleep(duration)
        for i in range(len(action)):
            releaseKey(action[i])

    else:
        raise TypeError('action needs to be an int or list')


if __name__ == '__main__':
    movements = [UP, LEFT, RIGHT, DOWN]
    durations = [0.05, 0.1, 0.15, 0.2, 0.25, 0.3, 0.35, 0.4]
    attacks = [LK, MK, HK, LP, MP, HP]
    time.sleep(8)
    while True:
        try:
            current_movement = movements[random.randint(0, len(movements))]
            executeAction(current_movement)
        except:
            do_nothing()
        try:
            current_attack = attacks[random.randint(0, len(attacks))]
            executeAction(current_attack)
        except:
            do_nothing()

        time.sleep(0.05)