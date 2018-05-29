import json
import sys
import threading
import keyboard
from tools import TextAnalyzer


class Listener(object):
    """" Listener object to capture keyboard input. """

    def __init__(self):
        self._esc_trigger = True
        self.keys_pressed = ''
        self._t = TextAnalyzer()

        self._start_listening()

    def _start_listening(self):
        """ Listen to keypresses until 'esc' is pressed. """

        while self._esc_trigger:
            self._key_pressed = keyboard.read_event()

            # t = threading.Thread(target=self._log_event, args=(self._key_pressed,))
            # t.start()
            self._log_event(self._key_pressed)

    def _log_event(self, event):
        """ Log pressed keyboard events (event_type == down). """

        e = event.to_json(ensure_ascii=sys.stdout.encoding != 'utf-8')
        self.e_json = json.loads(e)

        if self.e_json['event_type'] == 'down':
            if self.e_json['name'] == 'space' or self.e_json['name'] == 'enter':

                # to_print = 'You typed: {}'.format(self.keys_pressed)
                to_analyze = self.keys_pressed
                t = threading.Thread(target=self._t.analyze_text, args=(to_analyze,))
                t.start()
                # make_popup('You typed: {}'.format(to_print))
            
            self._store_key()

    def _store_key(self):
        """ Log pressed keyboard names as strings.
            Enter as delimiter, esc to end the run. """

        if self.e_json['name'] == 'space' or self.e_json['name'] == 'enter':
            self.keys_pressed = ''

        elif self.e_json['name'] == 'esc':
            self._esc_trigger = not self._esc_trigger
            self.keys_pressed = ''

        else:
            self.keys_pressed += self.e_json['name']

