import time
import threading
from .base import ObservableModel

import logging
logger = logging.getLogger(__name__)

class Stopwatch(ObservableModel):
    def __init__(self):
        super().__init__()
        self.started = False
        self.running = False
        self.reset = False
        self.passed = 0
    
    def change_stopwatch_state(self):
        if self.running:
            self.running = False
        else:
            self.running = True
            threading.Thread(target= lambda: self.trigger_event("count_stopwatch")).start()
            
    def update_stopwatch_view(self):
        if self.running:
            # self.stopwatch_label.after_cancel(self.update_time)
            self.running = False
        self.passed = 0
        self.trigger_event("update_stopwatch__view")
        # self.stopwatch_label.config(text=self.format_time_string(self.passed))
