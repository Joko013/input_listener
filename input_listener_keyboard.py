import keyboard
import json
import sys


class Listener(object):
    """" Listener object to capture keyboard input. """
    def __init__(self):
        self._start_listening()
        n=0
        while n < 3:
            
            self.keys_pressed = []
            self._wait_until_key(key='esc')
    
            typed_string = ''.join(event['name'] for event in self.keys_pressed[:-1])
            print(typed_string)
            n+=1
        
    def _wait_until_key(self, key):
        keyboard.wait(key)

    def _start_listening(self):
        """ Start listening after 'esc' is pressed. """
        self._wait_until_key(key='esc')
        keyboard.hook(self._log_event)

    def _log_event(self, event):
        e = event.to_json(ensure_ascii=sys.stdout.encoding != 'utf-8')
        e_json = json.loads(e)

        if e_json['event_type'] == 'down':
            self.keys_pressed.append(e_json)





