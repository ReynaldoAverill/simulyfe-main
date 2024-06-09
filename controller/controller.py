from .controller_userinterface import Controller_userinterface
from .controller_stopwatch import Controller_stopwatch
from .controller_page_main import Controller_page_main
from .controller_pump import Controller_pump
from .controller_base import Controller_base
from .controller_flow_sensor import Controller_flow_sensor
from .controller_force_sensor import Controller_force_sensor

from model.user_state import User_state
import model.constant as const

import sys
import logging

logger = logging.getLogger(__name__)

class Controller(Controller_base):
    def __init__(self,model, userinterface):
        super().__init__(model,userinterface)
        self.userinterface_controller = Controller_userinterface(self.model,self.userinterface)
        self.stopwatch_controller = Controller_stopwatch(self.model,self.userinterface)
        self.pump_controller = Controller_pump(self.model,self.userinterface)
        self.flow_sensor_controller = Controller_flow_sensor(self.model,self.userinterface)
        self.force_sensor_controller = Controller_force_sensor(self.model,self.userinterface)
        self.model.user_state.add_event_listener("exit_app",self.exit_app)

    def start_app(self):
        # create executable program of flow_sensor
        try:
            self.model.flow_sensor.trigger_event("generate_executable")
        except:
            logger.error("Flow sensor executable cannot be generated")
        try:
            self.model.force_sensor.activate_force_sensor()
        except:
            logger.error("Error when activating foce sensor")
        # Move to page main
        if self.model.user_state.state == "page_main":
            self.userinterface.switch_to("page_main")
            self.controller_page_main = Controller_page_main(self.model,self.userinterface)
        self.userinterface.start_mainloop()
    
    def exit_app(self,user_state: User_state):
        logger.critical("Processing to exit the app")
        if const.RASPBERRYPI:
            import RPi.GPIO as GPIO  # type: ignore
            GPIO.cleanup()
            self.model.pump.pwm.stop()
            logger.critical("GPIO pin cleaned and PWM stopped")
        # Mitigate interface destroyed multiple times
        try:
            self.userinterface.destroy_interface()
        except:
            logger.error("Window can't be destroyed")
        else:
            logger.critical("App interface destroyed")
        finally: 
            logger.critical("App closed")
            exit()
            