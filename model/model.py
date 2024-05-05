from .user_state import User_state
from .stopwatch import Stopwatch

class Model():
    def __init__(self):
        self.user_state = User_state()
        self.stopwatch = Stopwatch()
