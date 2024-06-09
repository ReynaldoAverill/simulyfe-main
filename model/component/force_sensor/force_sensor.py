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
        self.category_left: str         = "WEAK"

        self.force_sensor_right: HX711  = None
        self.longWithOffset_right: int  = 0
        self.weightValue_right: float   = 0
        self.category_right: str        = "WEAK"

    def activate_force_sensor(self):
        if const.RASPBERRYPI:
            self.trigger_event("activate_force_sensor")
    
    def retrieve_data(self):
        if const.RASPBERRYPI and const.ACTIVE_LEFT:
            self.trigger_event("retrieve_data_left")
        elif const.RASPBERRYPI and const.ACTIVE_RIGHT:
            self.trigger_event("retrieve_data_right")
        

    



     