import model.constant as const
from model.base import ObservableModel
from model.component.force_sensor.hx711 import HX711
import threading

import logging
logger = logging.getLogger(__name__)

class Force_sensor(ObservableModel):
    def __init__(self):
        super().__init__()
        self.force_sensor_left: HX711   = None
        self.longWithOffset_left: int   = 0
        self.weightValue_left: float    = 0
        self.category_left: str         = "NO FORCE"
        self.update_left                = False
        self.zero_left: float         = 0
        self.weight_adjusted_left: float    = 0
        self.strong_count_left          = 0
        self.medium_count_left          = 0
        self.safe_count_left            = 0
        self.noforce_count_left         = 0

        self.force_sensor_right: HX711  = None
        self.longWithOffset_right: int  = 0
        self.weightValue_right: float   = 0
        self.category_right: str        = "NO FORCE"
        self.update_right               = False
        self.zero_right: float         = 0
        self.weight_adjusted_right: float    = 0
        self.strong_count_right          = 0
        self.medium_count_right          = 0
        self.safe_count_right            = 0
        self.noforce_count_right         = 0

    def activate_force_sensor(self):
        if const.RASPBERRYPI:
            self.trigger_event("activate_force_sensor_left")
            self.trigger_event("activate_force_sensor_right")
    
    def retrieve_data(self):
        if const.RASPBERRYPI and const.ACTIVE_LEFT:
            self.update_left    = True
            thread_force_sensor_left = threading.Thread(target= lambda: self.trigger_event("retrieve_data_left"))
            # Auto close thread when main program ends
            thread_force_sensor_left.daemon = True
            thread_force_sensor_left.start()
        if const.RASPBERRYPI and const.ACTIVE_RIGHT:
            self.update_right   = True
            thread_force_sensor_right = threading.Thread(target= lambda: self.trigger_event("retrieve_data_right"))
            # Auto close thread when main program ends
            thread_force_sensor_right.daemon = True
            thread_force_sensor_right.start()
    
    def stop_retrieve_data(self):
        if self.update_left:
            self.update_left = False
            logger.info(f"LEFT Count | Strong = {self.strong_count_left} | Medium = {self.medium_count_left} | Safe = {self.safe_count_left} | No Force = {self.noforce_count_left}")
        if self.update_right:
            self.update_right = False
            logger.info(f"RIGHT Count | Strong = {self.strong_count_right} | Medium = {self.medium_count_right} | Safe = {self.safe_count_right} | No Force = {self.noforce_count_right}")

    def set_zero_left(self):
        self.zero_left = self.weightValue_left
        self.strong_count_left = 0
        self.medium_count_left = 0
        self.safe_count_left = 0
        self.noforce_count_left = 0
        logger.info(f"Zero value for left force sensor changed into {self.zero_left}. Reset category count")

    def set_zero_right(self):
        self.zero_right = self.weightValue_right
        self.strong_count_right = 0
        self.medium_count_right = 0
        self.safe_count_right = 0
        self.noforce_count_right = 0
        logger.info(f"Zero value for right force sensor changed into {self.zero_right}. Reset category count")

    



     