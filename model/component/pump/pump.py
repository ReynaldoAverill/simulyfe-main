import threading
from model.base import ObservableModel

import logging
logger = logging.getLogger(__name__)

class Pump(ObservableModel):
    def __init__(self):
        super().__init__()
        self.state  : bool = False
        self.pwm    : int = 0
        self.setpoint_debit :int = 0
        self.total_debit_digit: int = 0
        self.current_digit: int = 0
    
    def change_pump_state(self):
        if self.state:
            self.state = False
            logger.info("Pump turned off")
            self.trigger_event("change_button_layout")
        else:
            self.state = True
            logger.info("Pump turned on")
            threading.Thread(target= lambda: self.trigger_event("change_pump_state")).start()
    
    def change_pump_pwm(self, new_pwm):
        self.pwm = new_pwm
        
    def get_pump_setpoint_debit(self,new_number):
        if self.state:
            self.change_pump_state()
        self.current_digit = new_number
        self.trigger_event("get_pump_setpoint_debit")

    def delete_digit_setpoint_debit(self):
        if self.state:
            self.change_pump_state()
        self.trigger_event("delete_digit_setpoint_debit")

    def converter_setpoint_debit_to_pmw(self, set_point_debit):
        self.pwm = set_point_debit # need adjustment later