import numpy as np
from PIL import ImageGrab
import cv2
import time
import gc
import threading
import queue
import datetime

def unix_time_millis(dt):
    epoch = datetime.datetime.utcfromtimestamp(0)
    return int((dt - epoch).total_seconds() * 1000)

def screen_record():
    # 800x600 windowed mode
    printscreen =  np.array(ImageGrab.grab(bbox=(0,40,800,640)).convert('L'))
    return printscreen 

class screen_record_thread(threading.Thread):
    def __init__(self, in_q, f_name_q):
        threading.Thread.__init__(self)
        self.in_q = in_q
        self.f_name_q = f_name_q
        self.all_data = []
    def run(self):
        while True:
            try:
                stop_triggered = self.in_q.get(True, 0.0167)
                concat_data = np.stack(self.all_data, axis=2)
                f_name = 'D:\\sfv_game_data\\sfv_{}'.format(unix_time_millis(datetime.datetime.now()))
                np.save(f_name+'.npy', concat_data)
                print('data saved')
                self.f_name_q.put(f_name)
                del concat_data 
                self.all_data = []
                gc.collect()
                time.sleep(29)  
            except:
                self.all_data.append(screen_record())

if __name__ == '__main__':
    time.sleep(10)
    screen_record()