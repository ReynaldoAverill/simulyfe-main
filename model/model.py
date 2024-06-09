from .user_state import User_state
from .stopwatch import Stopwatch
from .component.pump.pump import Pump
from .component.flow_sensor.flow_sensor import Flow_sensor
from .component.camera.camera import Camera
import model.constant as const

class Model():
    def __init__(self):
        self.user_state = User_state()
        self.stopwatch = Stopwatch()
        self._create_component()
    
    def _create_component(self):
        self.pump   = Pump()
        self.flow_sensor    = Flow_sensor()
        self.camera = Camera()