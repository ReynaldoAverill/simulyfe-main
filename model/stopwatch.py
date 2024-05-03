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
            # self.trigger_event("count_stopwatch")
        
    # def count_stopwatch(self):
        # logger.debug("Start Stopwatch Count")
        # self.trigger_event("count_stopwatch")
        # start = time.time()
        # if self.started: # Case stopwatch already started
            # until_now = self.passed
        # else: # Case stopwatch not started yet
            # until_now = 0
            # self.started = True
        # while self.running:
            # self.passed = time.time() - start + until_now
