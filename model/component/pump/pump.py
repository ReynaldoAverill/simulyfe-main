import threading
import model.constant as const
from model.base import ObservableModel

import logging
logger = logging.getLogger(__name__)

class Pump(ObservableModel):
    def __init__(self):
        super().__init__()
        self.state  : bool = False
        self.duty_cycle    : int = 0
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
        self.duty_cycle = new_pwm
        
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
        self.duty_cycle = set_point_debit # need adjustment later

    def initiate_pump_gpio(self):
        if const.RASPBERRYPI:
            try:
                import RPi.GPIO as GPIO
            except:
                logger.error("GPIO cannot be defined. Import GPIO will be skipped")
            else:
                GPIO.setmode(GPIO.BCM)
                GPIO.setup(const.PIN_PWM,GPIO.OUT)
                GPIO.setup(const.PIN_PUMP_ENABLE_A, GPIO.OUT)
                GPIO.setup(const.PIN_PUMP_ENABLE_B, GPIO.OUT)
                self.pwm = GPIO(const.PIN_PWM,const.FREQ_PWM)
