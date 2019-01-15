import ctypes
import time
import random
import threading
import pynput
from pynput.keyboard import Key, Listener
import queue
from data_capture import screen_record_thread
from inputs import *


def main():
    time.sleep(10)

    in_q_actions = queue.Queue()
    in_q_recording = queue.Queue()
    # out_q = queue.Queue()

    random_actions = random_action_thread(in_q_actions)
    screen_recording = screen_record_thread(in_q_recording)
    random_actions.start()
    screen_recording.start()

    while True:
        with Listener(
            on_press = on_press,
            on_release = on_release) as listener:
            listener.join()
            in_q_actions.put(1)
            in_q_recording.put(1)
            time.sleep(30)


if __name__ == '__main__':
    main()