from .controller_base import Controller_base
from model.stopwatch import Stopwatch
from userinterface.page_anastomosis import Page_anastomosis
import time

import logging

logger = logging.getLogger(__name__)
    
class Controller_stopwatch(Controller_base):
    def __init__(self, model, userinterface) -> None:
        super().__init__(model,userinterface)
        self.stopwatch_page: Page_anastomosis = self.userinterface.current_page
        self.model.stopwatch.add_event_listener("count_stopwatch",self.count_stopwatch)
        self.model.stopwatch.add_event_listener("update_stopwatch_view",self.update_stopwatch_view)
    
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
            stopwatch.passed = time.time() - start + until_now
            self.update_stopwatch_view(stopwatch)
    
    def update_stopwatch_view(self, stopwatch: Stopwatch):
        # Renew current page to page_anastomosis with stopwatch
        self.stopwatch_page = self.userinterface.current_page
        # Calculate time and convert to string
        time_passed = stopwatch.passed
        seconds = time_passed % 60
        minutes = time_passed // 60
        hours   = minutes // 60
        stopwatch_string = f"{int(hours):02d}:{int(minutes):02d}:{int(seconds):02d}:{int(time_passed%1*100):02d}"
        self.stopwatch_page.itemconfigure(self.stopwatch_page.text_stopwatch,text=stopwatch_string)