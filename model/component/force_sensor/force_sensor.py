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
        self.update_left                = False

        self.force_sensor_right: HX711  = None
        self.longWithOffset_right: int  = 0
        self.weightValue_right: float   = 0
        self.category_right: str        = "WEAK"
        self.update_right               = False

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
        if self.update_right:
            self.update_right = False

    



     