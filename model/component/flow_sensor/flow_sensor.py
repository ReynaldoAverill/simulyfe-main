import threading
import model.constant as const
from model.base import ObservableModel

import logging
logger = logging.getLogger(__name__)

class Flow_sensor(ObservableModel):
    def __init__(self):
        super().__init__()
        self.state          = False
        self.measured_debit = 0
        self.debit_accuracy = 0
    
    def calculate_accuracy(self):
        if self.state:
            self.trigger_event("calculate_accuracy")

    