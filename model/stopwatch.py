import time
import threading
from .base import ObservableModel

import logging
logger = logging.getLogger(__name__)

class Stopwatch(ObservableModel):
    def __init__(self):
        super().__init__()
        self.started: bool = False
        self.running: bool = False
        self.reset  : bool = False
        self.passed = 0
    
    def change_stopwatch_state(self):
        if self.running:
            self.running = False
        else:
            self.running = True
            threading.Thread(target= lambda: self.trigger_event("count_stopwatch")).start()
            
    def reset_stopwatch(self):
        if self.running:
            self.running = False
        self.started = False
        self.passed = 0
        self.trigger_event("update_stopwatch_view")
        # self.stopwatch_label.config(text=self.format_time_string(self.passed))

