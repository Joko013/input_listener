import keyboard
import json
import sys


class Listener(object):
    """" Listener object to capture keyboard input. """
    def __init__(self):
        self.all_events = []
        self._start_listening()

        keyboard.wait('esc')

        typed_string = [event['name'] for event in self.all_events]
        print(typed_string)

    def _start_listening(self):
        keyboard.wait('esc')
        keyboard.hook(self._log_event)

    def _log_event(self, event):
        e = event.to_json(ensure_ascii=sys.stdout.encoding != 'utf-8')
        e_json = json.loads(e)

        if e_json['event_type'] == 'down':
            self.all_events.append(e_json)








