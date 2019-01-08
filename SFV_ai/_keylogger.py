import pythoncom, pyHook
from pyHook import KeyboardEvent  

class KeyLogger(object):
    def __init__(self):
        self.current_key = None

    def OnKeyboardEvent(self, event):
        # print('MessageName:',event.MessageName)
        # print('Message:',event.Message)
        # print('Time:',event.Time)
        # print('Window:',event.Window)
        # print('WindowName:',event.WindowName)
        # print('Ascii:', event.Ascii, chr(event.Ascii))
        # print('Key:', event.Key)
        # print('KeyID:', event.KeyID)
        # print('ScanCode:', event.ScanCode)
        # print('Extended:', event.Extended)
        # print('Injected:', event.Injected)
        # print('Alt', event.Alt)
        # print('Transition', event.Transition)
        # print('---')
        self.current_key = event.GetKey()

    # return True to pass the event to other handlers
        return True


if __name__ == '__main__':
    # create a hook manager
    hm = pyHook.HookManager()
    # watch for all mouse events
    keylogger = KeyLogger()
    hm.KeyDown = keylogger.OnKeyboardEvent
    print (keylogger.current_key)
    # set the hook
    hm.HookKeyboard()
    # wait forever
    pythoncom.PumpMessages()