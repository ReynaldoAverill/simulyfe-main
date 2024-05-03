from .controller_base import Controller_base
from model.stopwatch import Stopwatch
import time

import logging

logger = logging.getLogger(__name__)

def format_time_string(time_passed):
    seconds = time_passed % 60
    minutes = time_passed // 60
    hours   = minutes // 60
    return f"{int(hours):02d}:{int(minutes):02d}:{int(seconds):02d}:{int(time_passed%1*100):02d}"

class Controller_stopwatch(Controller_base):
    def __init__(self, model, userinterface) -> None:
        super().__init__(model,userinterface)
        self.model.stopwatch.add_event_listener("count_stopwatch",self.count_stopwatch)
    
    def count_stopwatch(self,stopwatch: Stopwatch):
        logger.info("Start Stopwatch Count")
        # self.trigger_event("count_stopwatch")
        start = time.time()
        if stopwatch.started: # Case stopwatch already started
            until_now = stopwatch.passed
        else: # Case stopwatch not started yet
            until_now = 0
            stopwatch.started = True
        while stopwatch.running:
            stopwatch_text = self.userinterface.current_page.text_stopwatch
            stopwatch.passed = time.time() - start + until_now
            self.userinterface.current_page.itemconfigure(stopwatch_text,text=format_time_string(stopwatch.passed))