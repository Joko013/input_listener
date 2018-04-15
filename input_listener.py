import pythoncom
import pyHook


class Listener(object):
    """" Listener object to capture keyboard input. """

    def __init__(self):
        self._return_pressed = False

        # listen to the keyboard
        self.hm = pyHook.HookManager()
        self.hm.KeyDown = self._on_keyboard_event
        self.hm.HookKeyboard()
        pythoncom.PumpMessages()

    def _on_keyboard_event(self, event):

        if event.Key == 'Return' and not self._return_pressed:
            self._return_pressed = not self._return_pressed
            self._text = ''

        elif event.Key == 'Return' and self._return_pressed:
            print(self._text)
            self._return_pressed = not self._return_pressed

        elif self._return_pressed:
            self._text += event.Key

        # return True to pass the event to other handlers
        return True

