import pythoncom
import pyHook


class Listener():
    def __init__(self):
        self.hm = pyHook.HookManager()
        self.hm.KeyDown = self._on_keyboard_event
        self.hm.HookKeyboard()
        pythoncom.PumpMessages()

    def _on_keyboard_event(self, event):
        if event.Key == 'Return':
            print('Nice, Return pressed')
        else:
            print('Return not pressed')

        # return True to pass the event to other handlers
        return True

