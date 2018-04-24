import keyboard
import json
import sys


class Listener(object):
    """" Listener object to capture keyboard input. """
    def __init__(self):
        self.keys_pressed = []
        self._start_listening()
        
        # here it should go like "on event X -> do Y" 
        # (ie. when Enter is pressed, start recording, stop when pressed again)        
        self._print_strings()
        
    def _wait_until_key(self, key):
        """ Wait (do not record keyboard) until a key is pressed."""
        keyboard.wait(key)

    def _start_listening(self):
        """ Start listening when 'enter' is pressed. """
        self._wait_until_key(key='enter')
        keyboard.hook(self._log_event)

    def _log_event(self, event):
        """ Log keyboard presses as keyboard events as json/dict to a list. """
        e = event.to_json(ensure_ascii=sys.stdout.encoding != 'utf-8')
        e_json = json.loads(e)

        if e_json['event_type'] == 'down':
            self.keys_pressed.append(e_json)

    def _print_strings(self):
        """ Print typed strings. """
        n=0
        while n < 3:
            self.keys_pressed = []
            self._wait_until_key(key='enter')            
            typed_string = ''.join(key['name'] for key in self.keys_pressed[:-1])
            print(typed_string)
            n+= 1
            


