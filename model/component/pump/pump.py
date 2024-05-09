import threading
from model.base import ObservableModel

class Pump(ObservableModel):
    def __init__(self):
        super().__init__()
        self.state  : bool = False
        self.pwm    : int = 0
        self.setpoint_debit :int = 0
        self.debit_digit: int = 0
    
    def change_pump_state(self):
        if self.state:
            self.state = False
        else:
            self.state = True
            threading.Thread(target= lambda: self.trigger_event("change_pump_state")).start()
    
    def change_pump_pwm(self, new_pwm):
        self.pwm = new_pwm

    def change_pump_setpoint_debit(self,new_setpoint_debit):
        self.setpoint_debit = new_setpoint_debit

    def converter_setpoint_debit_to_pmw(self, set_point_debit):
        self.pwm = set_point_debit # need adjustment later