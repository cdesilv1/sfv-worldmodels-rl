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
        print(len(all_data))
        print(all_data[-1].shape)
        cv2.imshow('window',cv2.cvtColor(printscreen, cv2.COLOR_BGR2RGB))
        k = cv2.waitKey(25) & 0xFF
        if k == ord('x'):
            cv2.destroyAllWindows()
            break

        concat_data = np.stack(all_data, axis=2)
        print(concat_data.shape)

if __name__ == '__main__':
    time.sleep(10)
    screen_record()