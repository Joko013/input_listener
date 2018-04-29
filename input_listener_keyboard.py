import keyboard
import json
import sys


class Listener(object):
    """" Listener object to capture keyboard input. """

    def __init__(self):
        self._start_listening()

        # here it should go like "on event X -> do Y"
        # (ie. when Enter is pressed, start recording, stop when pressed again)
        self._print_str()

    def _start_listening(self):
        """ Start listening when 'enter' is pressed. """
        self._enter_pressed = False
        self._esc_trigger = True

        keyboard.on_press(self._log_event)
        keyboard.wait('enter')

    def _log_event(self, event):
        """ Log pressed keyboard button names as strings. """
        e = event.to_json(ensure_ascii=sys.stdout.encoding != 'utf-8')
        self.e_json = json.loads(e)

        if self.e_json['name'] == 'enter' and not self._enter_pressed:
            self.keys_pressed = ''
            self._enter_pressed = not self._enter_pressed

        elif self.e_json['name'] == 'enter' and self._enter_pressed:
            self._enter_pressed = not self._enter_pressed

        elif self.e_json['name'] == 'esc':
            self._esc_trigger = not self._esc_trigger
            # keyboard.send('enter') # how to exit here?

        elif self._enter_pressed:
            self.keys_pressed += self.e_json['name']

    def _print_str(self):
        n = 0
        while self._esc_trigger:
            keyboard.wait('enter')
            self._enter_pressed = not self._enter_pressed
            print(self.keys_pressed)
            self.keys_pressed = ''
            n += 1

