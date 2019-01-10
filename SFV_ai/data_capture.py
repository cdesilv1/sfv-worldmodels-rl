import numpy as np
from PIL import ImageGrab
import cv2
import time

def screen_record():
    all_data = np.array()
    while(True):
        # 800x600 windowed mode
        printscreen =  np.array(ImageGrab.grab(bbox=(0,40,800,640)).convert('L'))
        print(printscreen.shape)
        # cv2.imshow('window',cv2.cvtColor(printscreen, cv2.COLOR_BGR2RGB))
        if cv2.waitKey(25) & 0xFF == ord('x'):
            cv2.destroyAllWindows()
            break

if __name__ == '__main__':
    screen_record()