from .user_state import User_state
from .stopwatch import Stopwatch
from .component.pump.pump import Pump

class Model():
    def __init__(self,linux = False):
        self.user_state = User_state()
        self.stopwatch = Stopwatch()
        if linux:
            self._create_component()
    
    def _create_component(self):
        self.pump = Pump()