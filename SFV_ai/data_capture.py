import numpy as np
from PIL import ImageGrab
import cv2
import time

def screen_record(): 
    while(True):
        # 800x600 windowed mode
        printscreen =  np.array(ImageGrab.grab(bbox=(0,40,800,640)))
        print(printscreen.shape)
        cv2.imshow('window',cv2.cvtColor(printscreen, cv2.COLOR_BGR2RGB))
        if cv2.waitKey(25) & 0xFF == ord('x'):
            cv2.destroyAllWindows()
            break
            