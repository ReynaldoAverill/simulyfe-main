from .controller_userinterface import Controller_userinterface
from .controller_stopwatch import Controller_stopwatch
from .controller_page_main import Controller_page_main
from model.model import Model
from userinterface.userinterface import Userinterface

import logging

logger = logging.getLogger(__name__)

class Controller:
    def __init__(self,model: Model, userinterface: Userinterface):
        self.model = model
        self.userinterface = userinterface
        self.userinterface_controller = Controller_userinterface(self.model,self.userinterface)
        self.stopwatch_controller = Controller_stopwatch(self.model,self.userinterface)

    def start_app(self):
        if self.model.user_state.state == "page_main":
            self.userinterface.switch_to("page_main")
            self.controller_page_main = Controller_page_main(self.model,self.userinterface)
        self.userinterface.start_mainloop()