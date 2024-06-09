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
        self.initiate_pump_gpio()
    
    def change_pump_state(self):
        if self.state:
            self.state = False
            logger.info("Pump turned off")
            self.trigger_event("turn_off_pump")
        else:
            self.state = True
            logger.info("Pump turned on")
            thread_pump = threading.Thread(target= lambda: self.trigger_event("turn_on_pump"))
            thread_pump.daemon = True
            thread_pump.start()
        
    def get_pump_setpoint_debit(self,new_number):
        if self.state:
            self.trigger_event("turn_off_pump")
            # self.change_pump_state()
        self.current_digit = new_number
        self.trigger_event("get_pump_setpoint_debit")

    def delete_digit_setpoint_debit(self):
        if self.state:
            self.trigger_event("turn_off_pump")
            # self.change_pump_state()
        self.trigger_event("delete_digit_setpoint_debit")

    def converter_setpoint_debit_to_pmw(self, set_point_debit):
        self.duty_cycle = set_point_debit # need adjustment later
                
    def reset_pump(self):
        """Reset pump to its initial condition
        """
        if self.state:
            self.state = False
        self.duty_cycle         = 0
        self.setpoint_debit     = 0
        self.total_debit_digit  = 0
        self.current_digit      = 0

    def initiate_pump_gpio(self):
        if const.RASPBERRYPI:
            try:
                import RPi.GPIO as GPIO # type: ignore
            except:
                logger.error("GPIO cannot be defined. Import GPIO will be skipped")
            else:
                GPIO.setmode(GPIO.BCM)
                GPIO.setup(const.PIN_PWM,GPIO.OUT)
                GPIO.setup(const.PIN_PUMP_ENABLE_A, GPIO.OUT)
                GPIO.setup(const.PIN_PUMP_ENABLE_B, GPIO.OUT)
                self.pwm: GPIO.PWM = GPIO.PWM(const.PIN_PWM,const.FREQ_PWM)
                self.pwm.start(self.duty_cycle)
