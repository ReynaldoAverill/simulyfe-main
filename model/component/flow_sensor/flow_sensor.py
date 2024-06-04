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
    
    def reset_flow_sensor(self):
        """Reset flow sensor to its initial condition
        """
        if self.state:
            self.state = False
        self.measured_debit     = 0
        self.debit_accuracy     = 0