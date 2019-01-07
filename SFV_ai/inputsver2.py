import ctypes
import time
import random
import threading
from _getcher import getKey

SendInput = ctypes.windll.user32.SendInput


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
THROW = [LP, LK]


#############################Directional Attacks#############################

LEFT_MP = [LEFT, MP] # Zugaihasatsu
RIGHT_MP = [RIGHT, MP] # Zugaihasatsu

LEFT_HP = [LEFT, HP] # Kikokuduki
RIGHT_HP = [RIGHT, HP] # Kikokuduki
DOWN_HP = [DOWN, HP]

DOWN_MK = [DOWN, MK] # Tenmakujinkyaku


#############################Miscellaneous Actions#############################

VTRIGGER = [HP, HK]

CHARGED_ATK = [MP, MK]

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


def executeAction(action, duration=0.0167): # Execute Keypresses
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


#############################Advanced Movement#############################

def QCR(DOWN=DOWN, RIGHT=RIGHT): # Quarter Circle Right
    pressKey(DOWN)
    time.sleep(0.0167)
    pressKey(RIGHT)
    time.sleep(0.0167)
    releaseKey(DOWN)
    time.sleep(0.0167)
    releaseKey(RIGHT)
    time.sleep(0.0167)


def QCL(DOWN=DOWN, LEFT=LEFT): # Quarter Circle Left
    pressKey(DOWN)
    time.sleep(0.0167)
    pressKey(LEFT)
    time.sleep(0.0167)
    releaseKey(DOWN)
    time.sleep(0.0167)
    releaseKey(LEFT)
    time.sleep(0.0167)

def HCR(LEFT=LEFT, DOWN=DOWN, RIGHT=RIGHT): # Half Circle Right
    pressKey(LEFT)
    time.sleep(0.0167)
    pressKey(DOWN)
    time.sleep(0.0167)
    releaseKey(LEFT)
    time.sleep(0.0167)
    pressKey(RIGHT)
    time.sleep(0.0167)
    releaseKey(DOWN)
    time.sleep(0.0167)
    releaseKey(RIGHT)
    time.sleep(0.0167)


def HCL(LEFT=LEFT, DOWN=DOWN, RIGHT=RIGHT): # Half Circle Left
    pressKey(RIGHT)
    time.sleep(0.0167)
    pressKey(DOWN)
    time.sleep(0.0167)
    releaseKey(RIGHT)
    time.sleep(0.0167)
    pressKey(LEFT)
    time.sleep(0.0167)
    releaseKey(DOWN)
    time.sleep(0.0167)
    releaseKey(LEFT)
    time.sleep(0.0167)

def DASH_LEFT(LEFT=LEFT):
    pressKey(LEFT)
    releaseKey(LEFT)
    time.sleep(0.0167)
    pressKey(LEFT)
    releaseKey(LEFT)
    time.sleep(0.0167)

def DASH_RIGHT(RIGHT=RIGHT):
    pressKey(RIGHT)
    releaseKey(RIGHT)
    time.sleep(0.0167)
    pressKey(RIGHT)
    releaseKey(RIGHT)
    time.sleep(0.0167)


#############################Advanced Attacks#############################

def HADOKEN_LEFT():
    QCL()
    executeAction(LP)
    time.sleep(0.05)

def HADOKEN_RIGHT():
    QCR()
    executeAction(LP)
    time.sleep(0.05)

def SHAKUNETSU_HADOKEN_LEFT():
    HCL()
    executeAction(LP)
    time.sleep(0.05)

def SHAKUNETSU_HADOKEN_RIGHT():
    HCR()
    executeAction(LP)
    time.sleep(0.05)

def SHORYUKEN_LEFT(LEFT=LEFT, DOWN=DOWN):
    pressKey(LEFT)
    time.sleep(0.0167)
    releaseKey(LEFT)
    time.sleep(0.0167)
    pressKey(DOWN)
    time.sleep(0.0167)
    releaseKey(DOWN)
    time.sleep(0.0167)
    pressKey(LEFT)
    pressKey(DOWN)
    time.sleep(0.0167)
    pressKey(LP)
    releaseKey(DOWN)
    releaseKey(LEFT)
    releaseKey(LP)
    time.sleep(0.05)

def SHORYUKEN_RIGHT(RIGHT=RIGHT, DOWN=DOWN):
    pressKey(RIGHT)
    time.sleep(0.0167)
    releaseKey(RIGHT)
    time.sleep(0.0167)
    pressKey(DOWN)
    time.sleep(0.0167)
    releaseKey(DOWN)
    time.sleep(0.0167)
    pressKey(RIGHT)
    pressKey(DOWN)
    time.sleep(0.0167)
    pressKey(LP)
    releaseKey(DOWN)
    releaseKey(RIGHT)
    releaseKey(LP)
    time.sleep(0.05)

def KUREKIJIN_LEFT():
    QCL()
    executeAction(LK)
    time.sleep(0.05)

def KUREKIJIN_RIGHT():
    QCR()
    executeAction(LK)
    time.sleep(0.05)

def RYUSOKYAKU_LEFT():
    HCL()
    executeAction(LK)
    time.sleep(0.05)

def RYUSOKYAKU_RIGHT():
    HCR()
    executeAction(LK)
    time.sleep(0.05)

def METSU_SHORYUKEN_LEFT():
    QCL()
    QCL()
    executeAction(LP)
    time.sleep(0.05)

def METSU_SHORYUKEN_RIGHT():
    QCR()
    QCR()
    executeAction(LP)
    time.sleep(0.05)

def SHORT_SPINKICK_LEFT():
    QCL()
    executeAction(LK)
    time.sleep(0.05)

def SHORT_SPINKICK_RIGHT():
    QCR()
    executeAction(LK)
    time.sleep(0.05)

def LONG_SPINKICK_LEFT():
    QCL()
    executeAction(MK)
    time.sleep(0.05)

def LONG_SPINKICK_RIGHT():
    QCR()
    executeAction(MK)
    time.sleep(0.05)


#############################Make Random Action#############################

def make_random_action():
    '''
    For the case of the randomized actions, actions will be chosen from a distribution as follows: movemements: 20%, attacks: 45%, special_attacks: 25%, trigger_moves: 5%, do_nothing: 5%
    movement durations will be chosen uniformly, and once a category is chosen, actions will be chosen uniformly
    randomized action category PDF was chosen arbitrarily
    '''

    movements = [UP, LEFT, RIGHT, DOWN, UP_LEFT, UP_RIGHT, DOWN_LEFT, DOWN_RIGHT, 'DASH_LEFT', 'DASH_RIGHT']

    durations = [0.05, 0.1, 0.15, 0.2, 0.25, 0.3, 0.35, 0.4, 0.45, 0.5, 0.55, 0.6, 0.65, 0.7, 0.75, 0.8]

    attacks = [LK, MK, HK, LP, MP, HP, LEFT_MP, RIGHT_MP, LEFT_HP, RIGHT_HP, DOWN_HP, THROW]

    special_attacks = [CHARGED_ATK, 'HADOKEN_LEFT', 'HADOKEN_RIGHT', 'SHAKUNETSU_HADOKEN_LEFT', 'SHAKUNETSU_HADOKEN_RIGHT', 'SHORYUKEN_LEFT',\
    'SHORYUKEN_RIGHT', 'KUREKIJIN_LEFT', 'KUREKIJIN_RIGHT', 'RYUSOKYAKU_LEFT', 'RYUSOKYAKU_RIGHT', 'SHORT_SPINKICK_LEFT',\
    'SHORT_SPINKICK_RIGHT', 'LONG_SPINKICK_LEFT', 'LONG_SPINKICK_RIGHT']

    trigger_moves = [VTRIGGER, 'METSU_SHORYUKEN_LEFT', 'METSU_SHORYUKEN_RIGHT']


    choose_action = random.randint(0, 101)
    if choose_action <=20:
        choice = random.choice(movements)
        if type(choice) is str:
            if choice == 'DASH_LEFT':
                DASH_LEFT()
            else:
                DASH_RIGHT()
        else:
            executeAction(choice, random.choice(durations))
    elif choose_action >20 and choose_action <=65:
        choice = random.choice(attacks)
        executeAction(choice)
    elif choose_action >65 and choose_action <=90:
        choice = random.choice(special_attacks)
        if type(choice) is str:
            if choice == 'HADOKEN_LEFT':
                HADOKEN_LEFT()
            elif choice == 'HADOKEN_RIGHT':
                HADOKEN_RIGHT()
            elif choice == 'SHAKUNETSU_HADOKEN_LEFT':
                SHAKUNETSU_HADOKEN_LEFT()
            elif choice == 'SHAKUNETSU_HADOKEN_RIGHT':
                SHAKUNETSU_HADOKEN_RIGHT()
            elif choice == 'SHORYUKEN_LEFT':
                SHORYUKEN_LEFT()
            elif choice == 'SHORYUKEN_RIGHT':
                SHORYUKEN_RIGHT()
            elif choice == 'KUREKIJIN_LEFT':
                KUREKIJIN_LEFT()
            elif choice == 'KUREKIJIN_RIGHT':
                KUREKIJIN_RIGHT()
            elif choice == 'RYUSOKYAKU_LEFT':
                RYUSOKYAKU_LEFT()
            elif choice == 'RYUSOKYAKU_RIGHT':
                RYUSOKYAKU_RIGHT()
            elif choice == 'SHORT_SPINKICK_LEFT':
                SHORT_SPINKICK_LEFT()
            elif choice == 'SHORT_SPINKICK_RIGHT':
                SHORT_SPINKICK_RIGHT()
            elif choice == 'LONG_SPINKICK_LEFT':
                LONG_SPINKICK_LEFT()
            else:
                LONG_SPINKICK_RIGHT()
        else:
            executeAction(choice)
    elif choose_action >90 and choose_action <=95:
        choice = random.choice(trigger_moves)
        if type(choice) is str:
            if choice == 'METSU_SHORYUKEN_LEFT':
                METSU_SHORYUKEN_LEFT()
            else:
                METSU_SHORYUKEN_RIGHT()
        else:
            executeAction(choice)
    else:
        do_nothing()
    time.sleep(0.0167)


#############################Threading Classes#############################

class random_action_thread(threading.Thread):
    def __init__(self, threadID):
        threading.Thread.__init__(self)
        self.threadID = threadID
        self.stop = 0
    def run(self):
        while True:
            if self.stop == 1:
                time.sleep(27) # TODO: tune sleep time for macro stopping point
                self.stop = 0
            make_random_action()

class getcher_thread(threading.Thread):
    def __init__(self, threadID, stopkey=b'65'):
        threading.Thread.__init__(self)
        self.threadID = threadID
        self.stopkey = stopkey
        self.stop = 0
    def run(self):
        while True:
            current_key = getKey()
            if current_key == self.stopkey:
                self.stop = 1
            


#############################__main__#############################

if __name__ == '__main__':
    getcher_thread = getcher_thread(0)
    random_action_thread = random_action_thread(1)

    getcher_thread.start()
    random_action_thread.start()
    while True:
        if getcher_thread.stop == 1:
            random_action_thread.stop = 1
            getcher_thread.stop = 0
    