import numpy as np
from PIL import ImageGrab
import cv2
import time
import gc 

def screen_record():
    all_data = []
    while(True):
        # 800x600 windowed mode
        printscreen =  np.array(ImageGrab.grab(bbox=(0,40,800,640)).convert('L'))
        all_data.append(printscreen)
        cv2.imshow('window',cv2.cvtColor(printscreen, cv2.COLOR_BGR2RGB))
        k = cv2.waitKey(10000) & 0xFF
        if k == ord('x'):
            cv2.destroyAllWindows()
            concat_data = np.stack(all_data, axis=2)
            print(concat_data.shape)
            break

if __name__ == '__main__':
    screen_record()