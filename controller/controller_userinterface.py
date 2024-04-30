from .controller_page_main import Controller_page_main
from .controller_page_anastomosis import Controller_page_anastomosis
from userinterface.userinterface import Userinterface
from model.model import Model
from model.user_state import User_state
import logging

logger = logging.getLogger(__name__)

class Controller_userinterface:
    def __init__(self, model:Model, userinterface: Userinterface):
        self.model = model
        self.userinterface = userinterface
        self.controller_page_main = Controller_page_main(self.model,self.userinterface)
        self.controller_page_anastomosis = Controller_page_anastomosis(self.model,self.userinterface)
        self.model.user_state.add_event_listener("move_to_page_anastomosis",self.move_to_page_anastomosis)
        self.model.user_state.add_event_listener("move_to_page_main",self.move_to_page_main)
        self.model.user_state.add_event_listener("exit_app",self.exit_app)

    def move_to_page_anastomosis(self,user_state: User_state):
        if user_state.state == "page_anastomosis":
            logger.debug("Move to Page Anastomosis")
            self.userinterface.switch_to(str(user_state.state))
            self.controller_page_main = Controller_page_anastomosis(self.model,self.userinterface)
    
    def move_to_page_main(self,user_state: User_state):
        if user_state.state == "page_main":
            logger.debug("Processing to Move to Page Main")
            self.userinterface.switch_to(user_state)
    
    def exit_app(self):
        logger.debug("Processing to close the app")
        self.userinterface.exit_app()

    def start_app(self):
        if self.model.user_state.state == "page_main":
            self.userinterface.switch_to("page_main")
            self.controller_page_main = Controller_page_main(self.model,self.userinterface)
        self.userinterface.start_mainloop()
        pass