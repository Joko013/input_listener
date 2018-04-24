import keyboard
import json
import sys


class Listener(object):
    """" Listener object to capture keyboard input. """

    def __init__(self):
        self._start_listening()

        # here it should go like "on event X -> do Y"
        # (ie. when Enter is pressed, start recording, stop when pressed again)

    def _start_listening(self):
        """ Start listening when 'enter' is pressed. """
        self._enter_pressed = False

        # keyboard.wait('enter')
        keyboard.hook(self._log_event)

        self._print_str()

    def _log_event(self, event):
        """ Log keyboard presses as keyboard events. """
        e = event.to_json(ensure_ascii=sys.stdout.encoding != 'utf-8')
        self.e_json = json.loads(e)

        trigger = False
        while not trigger:
            if self.e_json['event_type'] == 'down' and self.e_json['name'] == 'enter' and not self._enter_pressed:
                self.keys_pressed = ''
                self._enter_pressed = not self._enter_pressed

            elif self.e_json['event_type'] == 'down' and self.e_json['name'] == 'enter' and self._enter_pressed:
                print(self.keys_pressed)
                self._enter_pressed = not self._enter_pressed

            elif self.e_json['event_type'] == 'down' and self._enter_pressed:
                self.keys_pressed += self.e_json['name']

            elif self.e_json['event_type'] == 'down' and self.e_json['name'] == 'esc':
                trigger = not trigger

    def _print_str(self):
        n = 0
        while n < 3:
            self.keys_pressed = ''
            keyboard.wait('enter')
            typed_string = self.keys_pressed
            print(typed_string)
            n += 1
