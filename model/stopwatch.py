import time
import threading
from .base import ObservableModel

class Stopwatch(ObservableModel):
    def __init__(self):
        self.started = False
        self.running = False
        self.reset = False
        self.passed = 0
    
    def change_running_state(self):
        if self.running:
            self.running = False
        else:
            self.running = True
            threading.Thread(target=self.count_stopwatch).start()
        
    def count_stopwatch(self):
        start = time.time()
        if self.started: # Case stopwatch already started
            until_now = self.passed
        else: # Case stopwatch not started yet
            until_now = 0
            self.started = True
        while self.running:
            self.passed = time.time() - start + until_now
    
    def format_time_string(self, time_passed):
        seconds = time_passed % 60
        minutes = time_passed // 60
        hours   = minutes // 60
        return f"{int(hours):02d}:{int(minutes):02d}:{int(seconds):02d}:{int(self.passed%1*100):02d}"

